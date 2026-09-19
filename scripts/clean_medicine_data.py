from pathlib import Path

import pandas as pd


INPUT_FILE = Path("data/external/indian_medicine_data.csv")
OUTPUT_FILE = Path("data/processed/medicines_clean.csv")


def clean_text(value):
    if pd.isna(value):
        return None

    value = str(value).strip()

    if not value:
        return None

    return value


def main():
    print("Loading medicine dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Original rows: {len(df)}")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean text fields
    text_columns = [
        "name",
        "manufacturer_name",
        "type",
        "pack_size_label",
        "short_composition1",
        "short_composition2",
        "salt_composition",
        "medicine_desc",
        "side_effects",
        "drug_interactions",
    ]

    for column in text_columns:
        df[column] = df[column].apply(clean_text)

    # Normalize discontinued status
    df["Is_discontinued"] = df["Is_discontinued"].astype(bool)

    # Remove rows without a medicine name
    df = df.dropna(subset=["name"])

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Make sure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Cleaned rows: {len(df)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()