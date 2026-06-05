from sqlalchemy import create_engine

DB_USER = "nikhilsinghrathaur"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "security_master"

DATABASE_URL = f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

print("Database connected successfully!")