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


if __name__ == "__main__":
    create_database("data/taxi.duckdb")