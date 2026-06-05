from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()

engine = create_engine(
    "postgresql://nikhilsinghrathaur@localhost/security_master"
)

@app.get("/")
def home():
    return {"message": "Security Master API Running"}

@app.get("/prices")
def get_prices():

    query = """
    SELECT *
    FROM prices
    LIMIT 10
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")

@app.get("/health")
def health_check():
    return {"status": "healthy"}