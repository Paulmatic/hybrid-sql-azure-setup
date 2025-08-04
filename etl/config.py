import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Extract environment variables
AZURE_SQL_SERVER = os.getenv("AZURE_SQL_SERVER")
AZURE_SQL_DATABASE = os.getenv("AZURE_SQL_DATABASE")
AZURE_SQL_USERNAME = os.getenv("AZURE_SQL_USERNAME")
AZURE_SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD")
AZURE_SQL_PORT = os.getenv("AZURE_SQL_PORT", "1433")  # Default to 1433

# Validate
required_vars = [
    AZURE_SQL_SERVER, AZURE_SQL_DATABASE, AZURE_SQL_USERNAME, AZURE_SQL_PASSWORD
]
if not all(required_vars):
    raise EnvironmentError("❌ Missing one or more required environment variables.")

# Construct SQLAlchemy connection string
SQLALCHEMY_CONN_STRING = (
    f"mssql+pyodbc://{AZURE_SQL_USERNAME}:{AZURE_SQL_PASSWORD}"
    f"@{AZURE_SQL_SERVER}:{AZURE_SQL_PORT}/{AZURE_SQL_DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

print("✅ SQLAlchemy connection string is ready.")
