import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://nikhilsinghrathaur@localhost/security_master"
)

# Download data
df = yf.download("AAPL", period="1y")

# Reset index
df.reset_index(inplace=True)

# Flatten MultiIndex columns if they exist
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# Convert column names to lowercase
df.columns = [str(col).lower() for col in df.columns]

# Keep required columns
df = df[['date', 'open', 'high', 'low', 'close', 'volume']]

# Load into PostgreSQL
df.to_sql(
    "prices",
    engine,
    if_exists="replace",
    index=False
)

print(df.head())

print("\nData inserted successfully!")