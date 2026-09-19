from pathlib import Path

import pandas as pd


DATASET_PATH = Path("data/processed/medicines_clean.csv")


def search_medicines(query: str, limit: int = 10):
    query = query.strip().lower()

    if not query:
        return []

    df = pd.read_csv(DATASET_PATH)

    matches = df[
        df["name"]
        .str.lower()
        .str.contains(query, na=False)
    ].head(limit)

    return matches.to_dict(orient="records")