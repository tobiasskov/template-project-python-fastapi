import os
import sqlite3
import tempfile
from pathlib import Path
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from xyz_api.database.connection import init_db
from xyz_api.main import app


# Create a temporary database file for testing
@pytest.fixture(scope="session")
def test_db_path() -> Path:
    """Create a temporary database file for testing."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    # Create a database file in the temporary directory
    db_path = Path(temp_dir) / "test_vehicles.db"
    # Set the database path for testing
    os.environ["TEST_DB_PATH"] = str(db_path)
    return db_path


@pytest.fixture(scope="session")
def test_db(test_db_path: Path) -> Generator[sqlite3.Connection, None, None]:
    """Create a test database connection."""
    # Create a connection to the test database
    conn = sqlite3.connect(str(test_db_path))
    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        # Initialize the test database
        init_db()
        yield conn
    finally:
        # Close the connection
        conn.close()
        # Remove the test database file
        if test_db_path.exists():
            test_db_path.unlink()
        # Remove the temporary directory
        if test_db_path.parent.exists():
            test_db_path.parent.rmdir()


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client
