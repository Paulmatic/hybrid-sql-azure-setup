import pandas as pd

def transform_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    df['product_name'] = df['product_name'].str.strip()
    df['category'] = df['category'].str.title()
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['rating'] = df['rating'].fillna(0)
    df.drop_duplicates(inplace=True)

    print("✅ Transformed data")
    return df
