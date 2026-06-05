import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://nikhilsinghrathaur@localhost/security_master"
)

query = "SELECT * FROM prices"

df = pd.read_sql(query, engine)

st.title("Security Master Dashboard")

st.line_chart(df['close'])

st.dataframe(df.tail())