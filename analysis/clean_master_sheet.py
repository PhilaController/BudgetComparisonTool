import argparse
from pathlib import Path

import pandas as pd

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
        ]
        assert len(sheet_names) == 72

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

    # Save
    out_path = DATA_DIR / "processed" / f"{path.stem}.csv"
    result.to_csv(out_path, index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("start_year", type=int)
    parser.add_argument("kind", type=str, choices=["proposed", "adopted"])
    args = parser.parse_args()

    etl_data(args.start_year, args.kind)
