import datetime as dt

from sqlalchemy import text
from database import engine, init_db

# Create tables if they don't exist
init_db()


def run_sql(query: str):
    with engine.begin() as conn:
        result = conn.execute(text(query))

        if result.returns_rows:
            return result.fetchall()
        else:
            return result.rowcount


# Insert appointment
insert_query = """
INSERT INTO appointments
(patient_name, reason, start_time, cancelled, created_at, is_confirmed)
VALUES
(
    'Pandu',
    'Dental Checkup',
    '2026-06-25 10:00:00',
    0,
    CURRENT_TIMESTAMP,
    0
)
"""

print("Rows Inserted:", run_sql(insert_query))

# Fetch all appointments
select_query = "SELECT * FROM appointments"

appointments = run_sql(select_query)

print("\nAppointments:")
for appointment in appointments:
    print(appointment)