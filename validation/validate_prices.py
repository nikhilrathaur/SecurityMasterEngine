import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://nikhilsinghrathaur@localhost/security_master"
)

query = "SELECT * FROM prices"

df = pd.read_sql(query, engine)

# Calculate returns
df['returns'] = df['close'].pct_change()

# Fill NaN values
df['returns'] = df['returns'].fillna(0)

# Manual z-score calculation
mean_return = df['returns'].mean()
std_return = df['returns'].std()

df['zscore'] = (
    (df['returns'] - mean_return)
    / std_return
)

# Detect anomalies
anomalies = df[df['zscore'].abs() > 3]

print("\nAnomalies Detected:\n")
print(anomalies[['date', 'close', 'returns', 'zscore']])