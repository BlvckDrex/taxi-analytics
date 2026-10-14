from pathlib import Path

import duckdb


def create_database(db_path: str) -> None:
    """Create a DuckDB database and a raw schema."""

    Path(db_path).parent.mkdir(
        parents=True, exist_ok=True
    )

    with duckdb.connect(db_path) as conn:
        conn.execute(
            "CREATE SCHEMA IF NOT EXISTS raw"
        )

    print(f"Database initialized: {db_path}")


def load_taxi_data(db_path: str) -> None:
    """Load a sample of NYC taxi trips into DuckDB."""

    url = (
        "https://d37ci6vzurychx.cloudfront.net/"
        "trip-data/yellow_tripdata_2025-01.parquet"
    )

    with duckdb.connect(db_path) as conn:
        conn.execute("INSTALL httpfs;")
        conn.execute("LOAD httpfs;")

        conn.execute(
            """
            CREATE OR REPLACE TABLE raw.yellow_taxi_trips AS
            SELECT *
            FROM read_parquet(?)
            LIMIT 10000
            """,
            [url],
        )

        count = conn.execute(
            "SELECT COUNT(*) FROM raw.yellow_taxi_trips"
        ).fetchone()[0]

    print(f"Loaded {count} taxi trips")



if __name__ == "__main__":
    db_path = "data/taxi.duckdb"

    create_database(db_path)
    load_taxi_data(db_path)
