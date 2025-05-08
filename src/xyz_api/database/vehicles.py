import sqlite3
from datetime import date
from typing import List, Optional
from uuid import UUID, uuid4

from xyz_api.schemas.vehicles import (
    CarCreateV1,
    CarCreateV2,
    CarResponseV1,
    CarResponseV2,
    TruckCreateV1,
    TruckCreateV2,
    TruckResponseV1,
    TruckResponseV2,
    VehicleResponseV1,
    VehicleResponseV2,
)


def _date_to_str(d: Optional[date]) -> Optional[str]:
    """Convert a date object to ISO format string."""
    return d.isoformat() if d else None


def _str_to_date(s: Optional[str]) -> Optional[date]:
    """Convert an ISO format string to a date object."""
    return date.fromisoformat(s) if s else None


def create_car_v1(conn: sqlite3.Connection, car: CarCreateV1) -> CarResponseV1:
    """
    Create a new car in the database (V1).

    Args:
        conn: Database connection
        car: Car data to create

    Returns:
        CarResponseV1: Created car with generated ID
    """
    # Generate a new UUID
    car_id = str(uuid4())

    # Insert into vehicles table
    conn.execute(
        """
        INSERT INTO vehicles (
            id, make, model, year, color, vin, mileage, last_service_date,
            vehicle_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            car_id,
            car.make,
            car.model,
            car.year,
            car.color,
            car.vin,
            car.mileage,
            _date_to_str(car.last_service_date),
            "car",
        ),
    )

    # Insert into cars table
    conn.execute(
        """
        INSERT INTO cars (
            vehicle_id, doors, trunk_capacity, fuel_type, transmission
        ) VALUES (?, ?, ?, ?, ?)
    """,
        (
            car_id,
            car.doors,
            car.trunk_capacity,
            car.fuel_type.value,
            car.transmission.value,
        ),
    )

    # Commit the changes
    conn.commit()

    # Return the created car with the generated ID
    return CarResponseV1(id=UUID(car_id), **car.model_dump())


def create_car_v2(conn: sqlite3.Connection, car: CarCreateV2) -> CarResponseV2:
    """
    Create a new car in the database (V2).

    Args:
        conn: Database connection
        car: Car data to create

    Returns:
        CarResponseV2: Created car with generated ID
    """
    # Generate a new UUID
    car_id = str(uuid4())

    # Insert into vehicles table
    conn.execute(
        """
        INSERT INTO vehicles (
            id, make, model, year, color, vin, registration_number,
            insurance_expiry, is_available, vehicle_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            car_id,
            car.make,
            car.model,
            car.year,
            car.color,
            car.vin,
            car.registration_number,
            _date_to_str(car.insurance_expiry),
            car.is_available,
            "car",
        ),
    )

    # Insert into cars table
    conn.execute(
        """
        INSERT INTO cars (
            vehicle_id, doors, trunk_capacity, fuel_type, transmission,
            sunroof, parking_sensors
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            car_id,
            car.doors,
            car.trunk_capacity,
            car.fuel_type.value,
            car.transmission.value,
            car.sunroof,
            car.parking_sensors,
        ),
    )

    # Commit the changes
    conn.commit()

    # Return the created car with the generated ID
    return CarResponseV2(id=UUID(car_id), **car.model_dump())


def create_truck_v1(conn: sqlite3.Connection, truck: TruckCreateV1) -> TruckResponseV1:
    """
    Create a new truck in the database (V1).

    Args:
        conn: Database connection
        truck: Truck data to create

    Returns:
        TruckResponseV1: Created truck with generated ID
    """
    # Generate a new UUID
    truck_id = str(uuid4())

    # Insert into vehicles table
    conn.execute(
        """
        INSERT INTO vehicles (
            id, make, model, year, color, vin, mileage, last_service_date,
            vehicle_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            truck_id,
            truck.make,
            truck.model,
            truck.year,
            truck.color,
            truck.vin,
            truck.mileage,
            _date_to_str(truck.last_service_date),
            "truck",
        ),
    )

    # Insert into trucks table
    conn.execute(
        """
        INSERT INTO trucks (
            vehicle_id, bed_length, towing_capacity, payload_capacity,
            engine_size
        ) VALUES (?, ?, ?, ?, ?)
    """,
        (
            truck_id,
            truck.bed_length,
            truck.towing_capacity,
            truck.payload_capacity,
            truck.engine_size,
        ),
    )

    # Commit the changes
    conn.commit()

    # Return the created truck with the generated ID
    return TruckResponseV1(id=UUID(truck_id), **truck.model_dump())


def create_truck_v2(conn: sqlite3.Connection, truck: TruckCreateV2) -> TruckResponseV2:
    """
    Create a new truck in the database (V2).

    Args:
        conn: Database connection
        truck: Truck data to create

    Returns:
        TruckResponseV2: Created truck with generated ID
    """
    # Generate a new UUID
    truck_id = str(uuid4())

    # Insert into vehicles table
    conn.execute(
        """
        INSERT INTO vehicles (
            id, make, model, year, color, vin, registration_number,
            insurance_expiry, is_available, vehicle_type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            truck_id,
            truck.make,
            truck.model,
            truck.year,
            truck.color,
            truck.vin,
            truck.registration_number,
            _date_to_str(truck.insurance_expiry),
            truck.is_available,
            "truck",
        ),
    )

    # Insert into trucks table
    conn.execute(
        """
        INSERT INTO trucks (
            vehicle_id, bed_length, towing_capacity, payload_capacity,
            engine_size, four_wheel_drive, bed_liner
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            truck_id,
            truck.bed_length,
            truck.towing_capacity,
            truck.payload_capacity,
            truck.engine_size,
            truck.four_wheel_drive,
            truck.bed_liner,
        ),
    )

    # Commit the changes
    conn.commit()

    # Return the created truck with the generated ID
    return TruckResponseV2(id=UUID(truck_id), **truck.model_dump())


def get_all_vehicles_v1(conn: sqlite3.Connection) -> List[VehicleResponseV1]:
    """
    Get all vehicles from the database (V1).

    Args:
        conn: Database connection

    Returns:
        List[VehicleResponseV1]: List of all vehicles
    """
    # Query all vehicles
    cursor = conn.execute("""
        SELECT v.*, c.doors, c.trunk_capacity, c.fuel_type, c.transmission,
               t.bed_length, t.towing_capacity, t.payload_capacity, t.engine_size
        FROM vehicles v
        LEFT JOIN cars c ON v.id = c.vehicle_id
        LEFT JOIN trucks t ON v.id = t.vehicle_id
    """)

    vehicles = []
    for row in cursor:
        # Convert row to dictionary
        vehicle_data = dict(row)

        # Convert date strings to date objects
        vehicle_data["last_service_date"] = _str_to_date(
            vehicle_data["last_service_date"]
        )

        # Create appropriate response model based on vehicle type
        if vehicle_data["vehicle_type"] == "car":
            vehicles.append(
                CarResponseV1(
                    id=UUID(vehicle_data["id"]),
                    make=vehicle_data["make"],
                    model=vehicle_data["model"],
                    year=vehicle_data["year"],
                    color=vehicle_data["color"],
                    vin=vehicle_data["vin"],
                    mileage=vehicle_data["mileage"],
                    last_service_date=vehicle_data["last_service_date"],
                    doors=vehicle_data["doors"],
                    trunk_capacity=vehicle_data["trunk_capacity"],
                    fuel_type=vehicle_data["fuel_type"],
                    transmission=vehicle_data["transmission"],
                )
            )
        else:
            vehicles.append(
                TruckResponseV1(
                    id=UUID(vehicle_data["id"]),
                    make=vehicle_data["make"],
                    model=vehicle_data["model"],
                    year=vehicle_data["year"],
                    color=vehicle_data["color"],
                    vin=vehicle_data["vin"],
                    mileage=vehicle_data["mileage"],
                    last_service_date=vehicle_data["last_service_date"],
                    bed_length=vehicle_data["bed_length"],
                    towing_capacity=vehicle_data["towing_capacity"],
                    payload_capacity=vehicle_data["payload_capacity"],
                    engine_size=vehicle_data["engine_size"],
                )
            )

    return vehicles


def get_all_vehicles_v2(conn: sqlite3.Connection) -> List[VehicleResponseV2]:
    """
    Get all vehicles from the database (V2).

    Args:
        conn: Database connection

    Returns:
        List[VehicleResponseV2]: List of all vehicles
    """
    # Query all vehicles
    cursor = conn.execute("""
        SELECT v.*, c.doors, c.trunk_capacity, c.fuel_type, c.transmission,
               c.sunroof, c.parking_sensors,
               t.bed_length, t.towing_capacity, t.payload_capacity, t.engine_size,
               t.four_wheel_drive, t.bed_liner
        FROM vehicles v
        LEFT JOIN cars c ON v.id = c.vehicle_id
        LEFT JOIN trucks t ON v.id = t.vehicle_id
    """)

    vehicles = []
    for row in cursor:
        # Convert row to dictionary
        vehicle_data = dict(row)

        # Convert date strings to date objects
        vehicle_data["last_service_date"] = _str_to_date(
            vehicle_data["last_service_date"]
        )
        vehicle_data["insurance_expiry"] = _str_to_date(
            vehicle_data["insurance_expiry"]
        )

        # Create appropriate response model based on vehicle type
        if vehicle_data["vehicle_type"] == "car":
            vehicles.append(
                CarResponseV2(
                    id=UUID(vehicle_data["id"]),
                    make=vehicle_data["make"],
                    model=vehicle_data["model"],
                    year=vehicle_data["year"],
                    color=vehicle_data["color"],
                    vin=vehicle_data["vin"],
                    registration_number=vehicle_data["registration_number"],
                    insurance_expiry=vehicle_data["insurance_expiry"],
                    is_available=vehicle_data["is_available"],
                    doors=vehicle_data["doors"],
                    trunk_capacity=vehicle_data["trunk_capacity"],
                    fuel_type=vehicle_data["fuel_type"],
                    transmission=vehicle_data["transmission"],
                    sunroof=vehicle_data["sunroof"],
                    parking_sensors=vehicle_data["parking_sensors"],
                )
            )
        else:
            vehicles.append(
                TruckResponseV2(
                    id=UUID(vehicle_data["id"]),
                    make=vehicle_data["make"],
                    model=vehicle_data["model"],
                    year=vehicle_data["year"],
                    color=vehicle_data["color"],
                    vin=vehicle_data["vin"],
                    registration_number=vehicle_data["registration_number"],
                    insurance_expiry=vehicle_data["insurance_expiry"],
                    is_available=vehicle_data["is_available"],
                    bed_length=vehicle_data["bed_length"],
                    towing_capacity=vehicle_data["towing_capacity"],
                    payload_capacity=vehicle_data["payload_capacity"],
                    engine_size=vehicle_data["engine_size"],
                    four_wheel_drive=vehicle_data["four_wheel_drive"],
                    bed_liner=vehicle_data["bed_liner"],
                )
            )

    return vehicles
