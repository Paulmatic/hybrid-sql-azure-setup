import requests
import pandas as pd

def extract_sales_data() -> pd.DataFrame:
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data)
        df = df[['id', 'title', 'price', 'category', 'rating.rate']]
        df.rename(columns={
            'title': 'product_name',
            'rating.rate': 'rating'
        }, inplace=True)
        print("✅ Extracted data from API")
        return df
    else:
        raise Exception(f"❌ API call failed: {response.status_code}")

if __name__ == "__main__":
    df = extract_sales_data()
    df.to_csv("etl/sales_data.csv", index=False)
