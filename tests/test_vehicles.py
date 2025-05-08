# Test data
TEST_CAR_V1 = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2023,
    "color": "blue",
    "vin": "1HGCM82633A123456",
    "mileage": 0.0,
    "doors": 4,
    "trunk_capacity": 15.1,
    "fuel_type": "gasoline",
    "transmission": "automatic",
}

TEST_CAR_V2 = {
    "make": "Honda",
    "model": "Accord",
    "year": 2024,
    "color": "red",
    "vin": "2HGCM82633A123457",
    "registration_number": "ABC123",
    "insurance_expiry": "2025-12-31",
    "is_available": True,
    "doors": 4,
    "trunk_capacity": 16.0,
    "fuel_type": "hybrid",
    "transmission": "cvt",
    "sunroof": True,
    "parking_sensors": True,
}

TEST_TRUCK_V1 = {
    "make": "Ford",
    "model": "F-150",
    "year": 2023,
    "color": "black",
    "vin": "3HGCM82633A123458",
    "mileage": 0.0,
    "bed_length": 6.5,
    "towing_capacity": 5000.0,
    "payload_capacity": 2000.0,
    "engine_size": 3.5,
}

TEST_TRUCK_V2 = {
    "make": "Chevrolet",
    "model": "Silverado",
    "year": 2024,
    "color": "white",
    "vin": "4HGCM82633A123459",
    "registration_number": "XYZ789",
    "insurance_expiry": "2025-12-31",
    "is_available": True,
    "bed_length": 8.0,
    "towing_capacity": 8000.0,
    "payload_capacity": 2500.0,
    "engine_size": 5.3,
    "four_wheel_drive": True,
    "bed_liner": True,
}


# Test V1 Car Endpoints
def test_create_car_v1(client, test_db):
    """Test creating a car (V1)."""
    response = client.post("/api/v1/cars", json=TEST_CAR_V1)
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == TEST_CAR_V1["make"]
    assert data["model"] == TEST_CAR_V1["model"]
    assert data["year"] == TEST_CAR_V1["year"]
    assert data["color"] == TEST_CAR_V1["color"]
    assert data["vin"] == TEST_CAR_V1["vin"]
    assert data["mileage"] == TEST_CAR_V1["mileage"]
    assert data["doors"] == TEST_CAR_V1["doors"]
    assert data["trunk_capacity"] == TEST_CAR_V1["trunk_capacity"]
    assert data["fuel_type"] == TEST_CAR_V1["fuel_type"]
    assert data["transmission"] == TEST_CAR_V1["transmission"]
    assert "id" in data


def test_get_cars_v1(client, test_db):
    """Test getting all cars (V1)."""
    # Create a car first
    client.post("/api/v1/cars", json=TEST_CAR_V1)

    # Get all cars
    response = client.get("/api/v1/cars")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["make"] == TEST_CAR_V1["make"]
    assert data[0]["model"] == TEST_CAR_V1["model"]


# Test V1 Truck Endpoints
def test_create_truck_v1(client, test_db):
    """Test creating a truck (V1)."""
    response = client.post("/api/v1/trucks", json=TEST_TRUCK_V1)
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == TEST_TRUCK_V1["make"]
    assert data["model"] == TEST_TRUCK_V1["model"]
    assert data["year"] == TEST_TRUCK_V1["year"]
    assert data["color"] == TEST_TRUCK_V1["color"]
    assert data["vin"] == TEST_TRUCK_V1["vin"]
    assert data["mileage"] == TEST_TRUCK_V1["mileage"]
    assert data["bed_length"] == TEST_TRUCK_V1["bed_length"]
    assert data["towing_capacity"] == TEST_TRUCK_V1["towing_capacity"]
    assert data["payload_capacity"] == TEST_TRUCK_V1["payload_capacity"]
    assert data["engine_size"] == TEST_TRUCK_V1["engine_size"]
    assert "id" in data


def test_get_trucks_v1(client, test_db):
    """Test getting all trucks (V1)."""
    # Create a truck first
    client.post("/api/v1/trucks", json=TEST_TRUCK_V1)

    # Get all trucks
    response = client.get("/api/v1/trucks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["make"] == TEST_TRUCK_V1["make"]
    assert data[0]["model"] == TEST_TRUCK_V1["model"]


# Test V2 Car Endpoints
def test_create_car_v2(client, test_db):
    """Test creating a car (V2)."""
    response = client.post("/api/v2/cars", json=TEST_CAR_V2)
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == TEST_CAR_V2["make"]
    assert data["model"] == TEST_CAR_V2["model"]
    assert data["year"] == TEST_CAR_V2["year"]
    assert data["color"] == TEST_CAR_V2["color"]
    assert data["vin"] == TEST_CAR_V2["vin"]
    assert data["registration_number"] == TEST_CAR_V2["registration_number"]
    assert data["insurance_expiry"] == TEST_CAR_V2["insurance_expiry"]
    assert data["is_available"] == TEST_CAR_V2["is_available"]
    assert data["doors"] == TEST_CAR_V2["doors"]
    assert data["trunk_capacity"] == TEST_CAR_V2["trunk_capacity"]
    assert data["fuel_type"] == TEST_CAR_V2["fuel_type"]
    assert data["transmission"] == TEST_CAR_V2["transmission"]
    assert data["sunroof"] == TEST_CAR_V2["sunroof"]
    assert data["parking_sensors"] == TEST_CAR_V2["parking_sensors"]
    assert "id" in data


def test_get_cars_v2(client, test_db):
    """Test getting all cars (V2)."""
    # Create a car first
    client.post("/api/v2/cars", json=TEST_CAR_V2)

    # Get all cars
    response = client.get("/api/v2/cars")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["make"] == TEST_CAR_V2["make"]
    assert data[0]["model"] == TEST_CAR_V2["model"]


# Test V2 Truck Endpoints
def test_create_truck_v2(client, test_db):
    """Test creating a truck (V2)."""
    response = client.post("/api/v2/trucks", json=TEST_TRUCK_V2)
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == TEST_TRUCK_V2["make"]
    assert data["model"] == TEST_TRUCK_V2["model"]
    assert data["year"] == TEST_TRUCK_V2["year"]
    assert data["color"] == TEST_TRUCK_V2["color"]
    assert data["vin"] == TEST_TRUCK_V2["vin"]
    assert data["registration_number"] == TEST_TRUCK_V2["registration_number"]
    assert data["insurance_expiry"] == TEST_TRUCK_V2["insurance_expiry"]
    assert data["is_available"] == TEST_TRUCK_V2["is_available"]
    assert data["bed_length"] == TEST_TRUCK_V2["bed_length"]
    assert data["towing_capacity"] == TEST_TRUCK_V2["towing_capacity"]
    assert data["payload_capacity"] == TEST_TRUCK_V2["payload_capacity"]
    assert data["engine_size"] == TEST_TRUCK_V2["engine_size"]
    assert data["four_wheel_drive"] == TEST_TRUCK_V2["four_wheel_drive"]
    assert data["bed_liner"] == TEST_TRUCK_V2["bed_liner"]
    assert "id" in data


def test_get_trucks_v2(client, test_db):
    """Test getting all trucks (V2)."""
    # Create a truck first
    client.post("/api/v2/trucks", json=TEST_TRUCK_V2)

    # Get all trucks
    response = client.get("/api/v2/trucks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["make"] == TEST_TRUCK_V2["make"]
    assert data[0]["model"] == TEST_TRUCK_V2["model"]


# Test Error Cases
def test_create_car_invalid_vin_v1(client, test_db):
    """Test creating a car with invalid VIN (V1)."""
    invalid_car = TEST_CAR_V1.copy()
    invalid_car["vin"] = "invalid"  # VIN should be 17 characters
    response = client.post("/api/v1/cars", json=invalid_car)
    assert response.status_code == 422  # Validation error


def test_create_car_duplicate_vin_v1(client, test_db):
    """Test creating a car with duplicate VIN (V1)."""
    # Create first car
    client.post("/api/v1/cars", json=TEST_CAR_V1)

    # Try to create second car with same VIN
    response = client.post("/api/v1/cars", json=TEST_CAR_V1)
    assert response.status_code == 500  # Database error


def test_create_car_invalid_year_v1(client, test_db):
    """Test creating a car with invalid year (V1)."""
    invalid_car = TEST_CAR_V1.copy()
    invalid_car["year"] = 1800  # Year should be reasonable
    response = client.post("/api/v1/cars", json=invalid_car)
    assert response.status_code == 422  # Validation error
