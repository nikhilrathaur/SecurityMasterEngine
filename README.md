# Security Master & Market Data Validation Engine

A production-style financial data engineering project that builds a centralized Security Master system with automated market data validation, anomaly detection, ETL pipelines, APIs, and interactive dashboards.

---

# Project Overview

This project simulates the architecture used by financial institutions and quant teams to:

* ingest market data,
* validate data quality,
* detect anomalies,
* store normalized security data,
* expose APIs,
* and visualize analytics dashboards.

The system uses free and open-source tools and is designed as a portfolio-ready quant/data engineering project.

---

# Features

## Market Data Ingestion

* Pulls historical market data using Yahoo Finance
* Supports automated ETL workflows
* Stores data into PostgreSQL

## Security Master Database

* Centralized repository for market data
* PostgreSQL-backed architecture
* Structured schema for scalable storage

## Market Data Validation Engine

* Detects abnormal price movements
* Computes daily returns
* Performs z-score anomaly detection
* Identifies data quality issues

## Dashboard & Visualization

* Interactive Streamlit dashboard
* Price visualization
* Data preview and monitoring

## API Layer

* FastAPI-powered REST APIs
* Swagger API documentation
* Extensible backend architecture

---

# Tech Stack

| Component       | Technology                    |
| --------------- | ----------------------------- |
| Language        | Python                        |
| Database        | PostgreSQL                    |
| Data Processing | Pandas, NumPy                 |
| Market Data     | Yahoo Finance API             |
| Validation      | Statistical Z-Score Detection |
| Dashboard       | Streamlit                     |
| APIs            | FastAPI                       |
| ORM             | SQLAlchemy                    |
| Version Control | Git & GitHub                  |

---

# Project Structure

```bash
SecurityMasterEngine/
│
├── data/
├── database/
│   ├── db_connection.py
│   └── create_tables.py
│
├── etl/
│   ├── fetch_data.py
│   └── load_prices.py
│
├── validation/
│   └── validate_prices.py
│
├── dashboard/
│   └── app.py
│
├── api/
│   └── main.py
│
├── tests/
├── docs/
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SecurityMasterEngine.git
cd SecurityMasterEngine
```

---

# Create Virtual Environment

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install pandas numpy yfinance sqlalchemy psycopg2-binary streamlit fastapi uvicorn scipy plotly requests
```

---

# PostgreSQL Setup

Create PostgreSQL database:

```sql
CREATE DATABASE security_master;
```

---

# Run ETL Pipeline

```bash
cd etl
python3 load_prices.py
```

---

# Run Validation Engine

```bash
cd validation
python3 validate_prices.py
```

---

# Run Dashboard

```bash
cd dashboard
streamlit run app.py
```

---

# Run API

```bash
uvicorn api.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Example Workflow

```text
Yahoo Finance
      ↓
ETL Pipeline
      ↓
PostgreSQL Database
      ↓
Validation Engine
      ↓
Dashboard & APIs
```

---

# Future Improvements

* Multi-asset support
* Real-time streaming data
* Kafka integration
* Airflow scheduling
* Docker deployment
* Cloud infrastructure
* Advanced anomaly detection
* Corporate actions support
* Security identifier mapping

---

# Learning Outcomes

This project demonstrates:

* financial data engineering,
* ETL pipeline development,
* database architecture,
* quantitative validation,
* API development,
* dashboard creation,
* software engineering best practices.

---

# Author

Nikhil Singh Rathaur

GitHub: https://github.com/nikhilrathaur
