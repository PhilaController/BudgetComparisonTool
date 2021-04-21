import argparse
import shutil
from collections import OrderedDict
from pathlib import Path

import pandas as pd

DATA_DIR = Path(".") / "data"

CLASS_LABELS = OrderedDict(
    {
        "class_100": "Personal Services",
        "class_200": "Purchase of Services",
        "class_300_400": "Materials/Equip.",
        "class_500": "Contrib./Indemnities",
        "class_700": "Debt Service",
        "class_800": "Payments to Other Funds",
        "class_900": "Advances & Misc.",
    }
)

CODES = pd.read_excel(DATA_DIR / "raw" / "dept_code_reference.xlsx")


def format_data(df, cols_map):
    """Format the data we want to save."""

    return pd.merge(
        df[
            [
                "Code",
                "Expenditure Class",
            ]
            + list(cols_map.keys())
        ]
        .rename(
            columns={
                "Expenditure Class": "major_class_description",
            }
        )
        .rename(columns=cols_map)
        .query("major_class_description != 'total'")
        .assign(
            major_class_description=lambda df: df.major_class_description.replace(
                CLASS_LABELS
            )
        )
        .groupby(["Code", "major_class_description"])
        .sum()
        .reset_index(),
        CODES[
            ["Code", "dept_name", "category_code_description", "name"]
        ].drop_duplicates(),
        on="Code",
        how="left",
    )


def get_fy_tag(fiscal_year):
    """Return the last two digits of the input year."""
    return str(fiscal_year)[2:]


def get_file_path(start_year, kind):
    """Return the file path to load."""

    end_year = start_year + 4
    return (
        DATA_DIR
        / "processed"
        / f"FYP{get_fy_tag(start_year)}{get_fy_tag(end_year)}_Depts_{kind.capitalize()}.csv"
    )


def write_data(start_year, kind):
    """Write the cleaned data."""

    # Load the data for the current plan
    data = pd.read_csv(get_file_path(start_year, kind))

    # Rename the columns
    old_cols = [f"FY{get_fy_tag(start_year-1)} Adopted Budget"] + [
        f"FY{get_fy_tag(yr)} Estimate" for yr in range(start_year, start_year + 5)
    ]
    new_cols = [f"{start_year-1} (Adopted)"] + [
        f"{yr} ({kind.capitalize()})" for yr in range(start_year, start_year + 5)
    ]
    data = format_data(data, dict(zip(old_cols, new_cols)))

    # Load the data for last plan
    data2 = pd.read_csv(get_file_path(start_year - 1, "Adopted"))

    old_cols = [f"FY{get_fy_tag(start_year-2)} Adopted Budget"]
    new_cols = [f"{start_year-2} (Adopted)"]
    data2 = format_data(data2, dict(zip(old_cols, new_cols)))

    # Merge
    data = pd.merge(
        data,
        data2[["Code", "major_class_description", new_cols[0]]],
        on=["Code", "major_class_description"],
        how="left",
    )

    # Save data
    filename = (
        f"FYP{get_fy_tag(start_year)}{get_fy_tag(start_year+4)}-{kind}-by-major-class"
    )
    out_dir = DATA_DIR / "processed"
    json_path = out_dir / (filename + ".json")
    csv_path = out_dir / (filename + ".csv")

    # Save JSON and CSV
    data.drop(labels=["Code"], axis=1).to_json(json_path, orient="records")
    data.drop(labels=["Code"], axis=1).to_csv(csv_path, index=False)

    # Copy JSON file
    shutil.copy(json_path, Path("../src/data") / json_path.name)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("start_year", type=int)
    parser.add_argument("kind", type=str, choices=["proposed", "adopted"])
    args = parser.parse_args()

    write_data(args.start_year, args.kind)
