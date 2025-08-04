import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from etl.config import SQLALCHEMY_CONN_STRING

def load_dataframe_to_sql(df: pd.DataFrame, table_name: str):
    if df.empty:
        print("⚠️ DataFrame is empty. Nothing to load.")
        return

    try:
        engine = create_engine(SQLALCHEMY_CONN_STRING)
        with engine.begin() as conn:  # safer than .connect() for transactions
            df.to_sql(table_name, con=conn, if_exists='append', index=False, method='multi', chunksize=1000)
        print(f"✅ Loaded {len(df)} records to table: {table_name}")
    except SQLAlchemyError as e:
        print(f"❌ SQLAlchemy error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
