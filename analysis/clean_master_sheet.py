import argparse
import re
from pathlib import Path

import pandas as pd
from billy_penn.departments import load_city_departments

DATA_DIR = Path(".") / "data"


def validate(path, data):
    """Validate the results."""

    # Load the summary
    summary = pd.read_excel(
        path, sheet_name="Summary", nrows=9, skiprows=8, header=None, usecols="A:I"
    )
    summary.columns = data.columns[2:]
    summary = (
        summary.query("`Expenditure Class` == 'Total'")
        .filter(regex="^FY", axis=1)
        .sum()
    )

    # Sum
    totals = (
        data.query("`Expenditure Class` != 'total'").filter(regex="^FY", axis=1).sum()
    )

    # Check the difference
    diff = totals - summary
    assert (diff == 0).all()


def get_fy_tag(fiscal_year):
    """Return the last two digits of the input year."""
    return str(fiscal_year)[2:]


def read_dept_code(path, sheet_name):
    """Read the department code from a specific Excel sheet."""
    return tuple(
        pd.read_excel(
            path,
            sheet_name=sheet_name,
            header=None,
            nrows=1,
            usecols="B,C",
            dtype=str,
            skiprows=5,
        )
        .iloc[0]
        .tolist()
    )


def transform_data(df, start_year):
    """Put into phl-budget-data format."""

    col = f"FY{get_fy_tag(start_year)} Estimate"
    total = df.query("`Expenditure Class` == 'total'")[col].sum()

    # Load department info
    depts = load_city_departments(include_line_items=True)

    # Load master sheet crosswalk
    crosswalk = pd.read_excel("./data/raw/master-sheet-crosswalk.xlsx", dtype=str)

    # Merge dept info in
    crosswalk = crosswalk.merge(
        depts,
        on="dept_code",
        how="left",
    ).assign(dept_major_code=lambda df: df.dept_code.str.slice(0, 2))

    # Merge crosswalk
    df = (
        df.drop(columns="Code")
        .rename(columns={"Department": "dept_name_raw"})
        .merge(crosswalk, on="dept_name_raw", validate="m:1", how="left")
    )

    # Pivot it
    id_cols = [
        "dept_name_raw",
        "dept_code",
        "dept_name",
        "abbreviation",
        "dept_major_code",
    ]
    df = (
        df.set_index(id_cols)
        .pivot(columns="Expenditure Class", values=col)
        .reset_index()
    ).assign(fiscal_year=start_year)
    df.columns.name = None

    class_columns = [
        "class_100",
        "class_200",
        "class_300_400",
        "class_500",
        "class_700",
        "class_800",
        "class_900",
        "total",
    ]

    # Remove these
    # NOTE: this is done because some depts are broken out in the master sheets
    # but are not broken out in budget-in-brief. So, in order to compare to previous
    # year budget in briefs, we combine into main category
    NOT_BROKEN_OUT = ["55-L", "35-HTF"]
    for dept_code in NOT_BROKEN_OUT:

        sel = df["dept_code"] == dept_code
        if sel.sum():
            dept_major_code = dept_code[:2]
            sel2 = df["dept_code"] == dept_major_code  # Add to generic dept
            df.loc[sel2, class_columns] += df.loc[sel, class_columns].values
            df = df.loc[~sel]

    df = df.reset_index(drop=True)
    assert df["total"].sum() == total

    # Check missing
    missing = df.loc[df["dept_code"].isnull()]
    if len(missing):
        raise ValueError(
            f"Need to update 'master-sheet-crosswalk.xlsx'; Missing dept. info for: {missing['dept_name_raw'].tolist()}"
        )

    return df


def etl_data(start_year, kind):
    """Extract and clean the budget data."""

    # Create the filename
    end_year = start_year + 4
    path = (
        DATA_DIR
        / "raw"
        / f"FYP{get_fy_tag(start_year)}{get_fy_tag(end_year)}_Depts_{kind.capitalize()}.xlsx"
    )
    if not path.exists():
        raise FileNotFoundError(f"No such file '{str(path)}'")

    # get the sheet names
    with pd.ExcelFile(path) as ff:
        sheet_names = list(ff.sheet_names)

        # Remove first two summary sheets
        sheet_names = [
            name
            for name in sheet_names
            if not any(tag in name for tag in ["ALL", "TOTAL", "Summary", "Template"])
            and re.match("^[0-9]{2}", name)
        ]
        assert len(sheet_names) == 72, sorted(sheet_names)

    # Get th codes
    codes = [read_dept_code(path, sheet_name) for sheet_name in sheet_names]
    result = []

    # loop
    for i, sheet_name in enumerate(sheet_names):
        code = codes[i][0]
        dept_name = codes[i][1]

        # Read the data
        df = pd.read_excel(
            path,
            sheet_name=sheet_name,
            usecols="A:I",
        )

        code = str(df.iloc[4, 1]).strip().replace(" ", "").strip()
        if code == "35R" and "#32" in dept_name:
            code = "35REG"
        print(sheet_name, code, dept_name)

        dept_name = df.iloc[4, 2].strip()
        cols = [
            "Expenditure Class",
            f"FY{get_fy_tag(start_year-2)} Actual",
            f"FY{get_fy_tag(start_year-1)} Adopted Budget",
            f"FY{get_fy_tag(start_year-1)} Current Target",
        ]
        for fy in range(start_year, start_year + 5):
            cols.append(
                f"FY{get_fy_tag(fy)} Estimate",
            )

        df = df.iloc[7:].iloc[:8]
        df.columns = cols

        # read this sheet
        result.append(df.assign(Department=dept_name, Code=code))

        result[-1]["Expenditure Class"] = [
            "class_100",
            "class_200",
            "class_300_400",
            "class_500",
            "class_700",
            "class_800",
            "class_900",
            "total",
        ]

    # Combine the results from each dept
    result = pd.concat(result, sort=True).fillna(0).reset_index(drop=True)

    # Validate!
    validate(path, result)

    # Save unformatted
    out_path = DATA_DIR / "processed" / "master_sheets_original" / f"{path.stem}.csv"
    result.to_csv(out_path, index=False)

    # Format
    result = transform_data(result, start_year)
    out_path = (
        DATA_DIR
        / "processed"
        / "master_sheets_transformed"
        / f"FY{get_fy_tag(start_year)}-{kind}.csv"
    )
    result.to_csv(out_path, index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("start_year", type=int)
    parser.add_argument("kind", type=str, choices=["proposed", "adopted"])
    args = parser.parse_args()

    etl_data(args.start_year, args.kind)
