import os

import psycopg
from dotenv import load_dotenv

# Load the connection settings from .env.
load_dotenv()


def get_connection():
    # Open a connection to PostgreSQL.
    return psycopg.connect(
        host=os.environ["POSTGRES_HOST"],
        port=int(os.environ["POSTGRES_PORT"]),
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        connect_timeout=5,
    )





if __name__ == "__main__":
    with get_connection() as connection:
        result = connection.execute(
            "SELECT current_database();"
        ).fetchone()

        if result is None:
            raise RuntimeError("The query returned no result.")

        print("Connected successfully to:", result[0])


