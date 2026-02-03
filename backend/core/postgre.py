import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv
from psycopg2.pool import ThreadedConnectionPool

dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

pool = ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    dsn=DATABASE_URL
)

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS user_data (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    video_id TEXT NOT NULL,
    title TEXT NOT NULL,
    watched_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

def create_tables():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        cur = conn.cursor()
        cur.execute(CREATE_TABLE_QUERY)
        conn.commit()
        print("Table created.")
    finally:
        conn.close()

def get_connection():
    return pool.getconn()

def release_connection(conn):
    pool.putconn(conn)

if __name__ == "__main__":
    create_tables()   
