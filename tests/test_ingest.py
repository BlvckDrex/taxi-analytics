import duckdb

from src.ingest import create_database


def test_create_database(tmp_path):
    db_path = tmp_path / "test.duckdb"

    create_database(str(db_path))

    assert db_path.exists()

    with duckdb.connect(str(db_path)) as conn:
        schemas = conn.execute(
            "SELECT schema_name "
            "FROM information_schema.schemata"
        ).fetchall()

    assert ("raw",) in schemas