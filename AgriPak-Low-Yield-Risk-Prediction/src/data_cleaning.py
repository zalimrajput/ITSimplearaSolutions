
import os
import pandas as pd


def clean_dataset(input_path, output_path, target_column):

    df = pd.read_csv(input_path)

    original_rows = len(df)

    df.columns = df.columns.astype(str).str.strip()

    if target_column not in df.columns:
        raise ValueError(
            f"Target {target_column} not found."
        )

    df[target_column] = pd.to_numeric(
        df[target_column],
        errors="coerce"
    )

    missing_target = df[target_column].isna().sum()

    df = df.dropna(
        subset=[target_column]
    ).copy()

    if not set(df[target_column].unique()).issubset({0, 1}):
        raise ValueError(
            "Target must contain only 0 and 1."
        )

    df[target_column] = df[target_column].astype(int)

    if df[target_column].nunique() != 2:
        raise ValueError(
            "Both target classes must be present."
        )

    duplicates = df.duplicated().sum()

    df = df.drop_duplicates().copy()

    for col in df.columns:

        if col == target_column:
            continue

        if df[col].dtype == "object":

            converted = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            count = df[col].notna().sum()

            if count > 0:

                ratio = converted.notna().sum() / count

                if ratio >= 0.90:
                    df[col] = converted

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    df.to_csv(
        output_path,
        index=False
    )

    print("Original records:", original_rows)
    print("Cleaned records:", len(df))
    print("Missing targets removed:", missing_target)
    print("Duplicate records removed:", duplicates)

    return df


if __name__ == "__main__":

    clean_dataset(
        "data/raw/crop_data.csv",
        "data/processed/cleaned_data.csv",
        "low_yield_risk"
    )
