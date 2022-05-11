import os

import numpy as np
import pandas as pd

csv_shoot = os.path.abspath("shoot/Results.csv")
json_shoot = os.path.abspath("temp/results.json")


def clean_shoot():
    df_results = pd.read_csv(csv_shoot)

    columns = []

    common_columns = [
        "File #",
        "DateTime",
        "Operator",
        "Application",
        "Method",
        "Alloy 1",
    ]

    important_elements = [
        "Au",
        "Ag",
        "Cu",
        "Zn",
        "Pt",
        "Pd",
        "Rh",
        "Ru",
        "Fe",
        "Rh",
        "Sn",
        "Pb",
        "Ni",
        "W",
    ]

    header = df_results.columns
    elements = header.intersection(important_elements)

    columns = list(common_columns) + list(elements)

    clean_df = df_results[columns]
    clean_df = clean_df.fillna(np.nan)
    clean_df = clean_df.replace({"< LOD": np.nan})
    clean_df = clean_df.dropna(axis="columns")

    clean_df.to_json(json_shoot, orient="records")
