import argparse
from pathlib import Path

import pandas as pd
from billy_penn.departments import load_city_departments

GITHUB = "https://raw.githubusercontent.com/PhilaController/phl-budget-data/main/src/phl_budget_data/data/processed/spending"
START_FISCAL_YEAR = 2020

MAJOR_CLASS_DESCRIPTIONS = {
    "class_900": "Advances & Misc.",
    "class_500": "Contrib./Indemnities",
    "class_700": "Debt Service",
    "class_300_400": "Materials/Equip.",
    "class_800": "Payments to Other Funds",
    "class_100": "Personal Services",
    "class_200": "Purchase of Services",
}


def load_data(kind):
    """Load the data"""

    # Raw data
    df = pd.read_csv(f"{GITHUB}/budgeted-department-spending-{kind}.csv")

    # Load any parsed master sheets too
    path = Path("./data/processed/master_sheets_transformed/")
    files = path.glob(f"*-{kind}.csv")
    for f in files:
        x = pd.read_csv(f, dtype={"dept_code": str, "dept_major_code": str})
        df = pd.concat([df, x], axis=0, ignore_index=True)

        # IMPORTANT: Drop duplicates
        df = df.drop_duplicates(subset=["dept_code", "fiscal_year"], keep="first")

    # Merge categories
    categories = load_categories()
    df = df.merge(categories, on="dept_code", how="left").assign(
        dept_major_code=lambda df: df["dept_code"].str.slice(0, 2)
    )

    # Merge depts
    depts = load_city_departments().rename(columns={"dept_code": "dept_major_code"})

    return (
        df.rename(columns={"dept_name": "name"})
        .drop(columns=["abbreviation"])
        .merge(depts, on="dept_major_code", how="left")
        .rename(columns={"category_major": "category_code_description"})
    )


def load_categories():
    return pd.read_excel("./data/raw/dept-categories.xlsx").drop(
        columns=["dept_name", "abbreviation"]
    )


def transform_data(df, fy, kind):

    df = df.query(f"fiscal_year == {fy}").drop(columns=["fiscal_year"])
    if not len(df):
        return None

    id_cols = ["dept_name", "name", "category_code_description"]
    return (
        df.groupby(id_cols)
        .sum()
        .drop(columns=["total"])
        .reset_index()
        .melt(
            id_vars=id_cols,
            value_name=f"{fy} ({kind})",
            var_name="major_class_description",
        )
        .assign(
            major_class_description=lambda df: df.major_class_description.replace(
                MAJOR_CLASS_DESCRIPTIONS
            )
        )
    )


def main(current_fiscal_year, kind):
    """Process the data."""

    # Load the data
    adopted = load_data("adopted")
    proposed = load_data("proposed")

    data = None
    for fy in range(START_FISCAL_YEAR, current_fiscal_year):

        for tag, df in zip(["Adopted", "Proposed"], [adopted, proposed]):
            X = transform_data(df, fy, tag)
            if X is None:
                continue
            if data is None:
                data = X
            else:
                data = data.merge(
                    X,
                    on=[
                        "dept_name",
                        "name",
                        "category_code_description",
                        "major_class_description",
                    ],
                    how="outer",
                )

    # Add proposed if current year is adopted
    if kind == "adopted":
        X = transform_data(proposed, current_fiscal_year, "Proposed")
        data = data.merge(
            X,
            on=[
                "dept_name",
                "name",
                "category_code_description",
                "major_class_description",
            ],
            how="outer",
        )

    # Add current year
    if kind == "adopted":
        df = adopted
    else:
        df = proposed

    X = transform_data(df, current_fiscal_year, kind.capitalize())
    data = data.merge(
        X,
        on=[
            "dept_name",
            "name",
            "category_code_description",
            "major_class_description",
        ],
        how="outer",
    )

    # Add aliases
    dept_aliases = pd.read_excel("./data/raw/dept-aliases.xlsx")
    dept_alias_dict = dict(zip(dept_aliases["dept_name"], dept_aliases["alias"]))
    data["dept_name"] = data["dept_name"].replace(dept_alias_dict)

    name_aliases = pd.read_excel("./data/raw/name-aliases.xlsx")
    name_alias_dict = dict(zip(name_aliases["name"], name_aliases["alias"]))
    data["name"] = data["name"].replace(name_alias_dict)

    return data.fillna(0)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "fiscal_year", type=int, help="The current fiscal year to process"
    )
    parser.add_argument("kind", choices=["adopted", "proposed"])

    # Get the data
    args = parser.parse_args()
    data = main(args.fiscal_year, args.kind)

    # Save it
    filename = "budget-comparison-data"
    data.to_json(f"./data/processed/{filename}.json", orient="records")
    data.to_csv(f"./data/processed/{filename}.csv", index=False)
    data.to_json(f"../src/data/{filename}.json", orient="records")
