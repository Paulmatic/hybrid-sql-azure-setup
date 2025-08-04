from etl.extract_api import extract_sales_data
from etl.transform_data import transform_sales_data
from etl.qa_checks import run_data_quality_checks
from etl.load_to_sql import load_dataframe_to_sql

def run_etl():
    try:
        print("🚀 Starting ETL process...")
        df = extract_sales_data()
        df = transform_sales_data(df)
        run_data_quality_checks(df)
        load_dataframe_to_sql(df, table_name="sales_data")
        print("🎉 ETL pipeline complete!")
    except Exception as e:
        print(f"❌ ETL pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_etl()
