from sqlalchemy import text
from db_connection import engine

query = """
CREATE TABLE IF NOT EXISTS prices (
    id SERIAL PRIMARY KEY,
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT
);
"""

with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()

print("Table created!")