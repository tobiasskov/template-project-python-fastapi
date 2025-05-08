import sqlite3
from pathlib import Path
from typing import Generator

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
# Database file will be stored in the project root
DB_PATH = PROJECT_ROOT / "vehicles.db"


def get_db_connection() -> sqlite3.Connection:
    """
    Create and return a new database connection.

    Returns:
        sqlite3.Connection: A connection to the SQLite database.
    """
    # Create a connection to the SQLite database
    # The database file will be created if it doesn't exist
    conn = sqlite3.connect(str(DB_PATH))
    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")
    # Return the connection
    return conn


def init_db() -> None:
    """
    Initialize the database by creating necessary tables.
    This function should be called when the application starts.
    """
    # Get a database connection
    conn = get_db_connection()
    try:
        # Create the vehicles table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                id TEXT PRIMARY KEY,  -- UUID as text
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                color TEXT NOT NULL,
                vin TEXT NOT NULL UNIQUE,
                mileage REAL NOT NULL,
                last_service_date TEXT,  -- ISO format date string
                registration_number TEXT,
                insurance_expiry TEXT,  -- ISO format date string
                is_available BOOLEAN NOT NULL DEFAULT 1,
                vehicle_type TEXT NOT NULL  -- 'car' or 'truck'
            )
        """)

        # Create the cars table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                vehicle_id TEXT PRIMARY KEY,
                doors INTEGER NOT NULL,
                trunk_capacity REAL NOT NULL,
                fuel_type TEXT NOT NULL,
                transmission TEXT NOT NULL,
                sunroof BOOLEAN NOT NULL DEFAULT 0,
                parking_sensors BOOLEAN NOT NULL DEFAULT 0,
                FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
            )
        """)

        # Create the trucks table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS trucks (
                vehicle_id TEXT PRIMARY KEY,
                bed_length REAL NOT NULL,
                towing_capacity REAL NOT NULL,
                payload_capacity REAL NOT NULL,
                engine_size REAL NOT NULL,
                four_wheel_drive BOOLEAN NOT NULL DEFAULT 0,
                bed_liner BOOLEAN NOT NULL DEFAULT 0,
                FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
            )
        """)

        # Commit the changes
        conn.commit()
    finally:
        # Always close the connection
        conn.close()


def get_db() -> Generator[sqlite3.Connection, None, None]:
    """
    Get a database connection for use in FastAPI dependency injection.

    Yields:
        sqlite3.Connection: A connection to the SQLite database.
    """
    conn = get_db_connection()
    try:
        yield conn
    finally:
        conn.close()
