import pandas as pd

def run_data_quality_checks(df: pd.DataFrame):
    errors = []

    if df.isnull().any().any():
        errors.append("❌ Data contains NULL values")

    if not df['price'].between(1, 10000).all():
        errors.append("❌ One or more prices are out of the expected range (1 - 10,000)")

    if not df['rating'].between(0, 5).all():
        errors.append("❌ One or more ratings are out of the expected range (0 - 5)")

    if errors:
        for error in errors:
            print(error)
        raise ValueError("❌ Data quality checks failed!")
    else:
        print("✅ Data passed all quality checks")
