
import duckdb

with duckdb.connect("data/taxi.duckdb") as conn:
    result = conn.execute(
        """
        SELECT
            COUNT(*) AS total_trips,
            ROUND(AVG(trip_distance), 2) AS avg_distance,
            ROUND(AVG(fare_amount), 2) AS avg_fare
        FROM raw.yellow_taxi_trips
        """
    ).fetchall()

print(result)
