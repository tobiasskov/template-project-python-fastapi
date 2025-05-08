import sqlite3

from fastapi import APIRouter, Depends

from xyz_api.database.connection import get_db
from xyz_api.database.vehicles import (
    create_car_v1,
    create_car_v2,
    create_truck_v1,
    create_truck_v2,
    get_all_vehicles_v1,
    get_all_vehicles_v2,
)
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

# Version 1 router
v1_router = APIRouter(prefix="/api/v1")


@v1_router.get("/vehicles", response_model=list[VehicleResponseV1])
async def get_vehicles_v1(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of vehicles (V1)."""
    return get_all_vehicles_v1(conn)


@v1_router.post("/vehicles", response_model=VehicleResponseV1)
async def create_vehicle_v1(
    vehicle: CarCreateV1 | TruckCreateV1, conn: sqlite3.Connection = Depends(get_db)
):
    """Create a new vehicle (V1)."""
    if isinstance(vehicle, CarCreateV1):
        return create_car_v1(conn, vehicle)
    return create_truck_v1(conn, vehicle)


@v1_router.get("/cars", response_model=list[CarResponseV1])
async def get_cars_v1(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of cars (V1)."""
    vehicles = get_all_vehicles_v1(conn)
    return [v for v in vehicles if isinstance(v, CarResponseV1)]


@v1_router.post("/cars", response_model=CarResponseV1)
async def create_car_v1(car: CarCreateV1, conn: sqlite3.Connection = Depends(get_db)):
    """Create a new car (V1)."""
    return create_car_v1(conn, car)


@v1_router.get("/trucks", response_model=list[TruckResponseV1])
async def get_trucks_v1(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of trucks (V1)."""
    vehicles = get_all_vehicles_v1(conn)
    return [v for v in vehicles if isinstance(v, TruckResponseV1)]


@v1_router.post("/trucks", response_model=TruckResponseV1)
async def create_truck_v1(
    truck: TruckCreateV1, conn: sqlite3.Connection = Depends(get_db)
):
    """Create a new truck (V1)."""
    return create_truck_v1(conn, truck)


# Version 2 router
v2_router = APIRouter(prefix="/api/v2")


@v2_router.get("/vehicles", response_model=list[VehicleResponseV2])
async def get_vehicles_v2(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of vehicles (V2)."""
    return get_all_vehicles_v2(conn)


@v2_router.post("/vehicles", response_model=VehicleResponseV2)
async def create_vehicle_v2(
    vehicle: CarCreateV2 | TruckCreateV2, conn: sqlite3.Connection = Depends(get_db)
):
    """Create a new vehicle (V2)."""
    if isinstance(vehicle, CarCreateV2):
        return create_car_v2(conn, vehicle)
    return create_truck_v2(conn, vehicle)


@v2_router.get("/cars", response_model=list[CarResponseV2])
async def get_cars_v2(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of cars (V2)."""
    vehicles = get_all_vehicles_v2(conn)
    return [v for v in vehicles if isinstance(v, CarResponseV2)]


@v2_router.post("/cars", response_model=CarResponseV2)
async def create_car_v2(car: CarCreateV2, conn: sqlite3.Connection = Depends(get_db)):
    """Create a new car (V2)."""
    return create_car_v2(conn, car)


@v2_router.get("/trucks", response_model=list[TruckResponseV2])
async def get_trucks_v2(conn: sqlite3.Connection = Depends(get_db)):
    """Retrieve a list of trucks (V2)."""
    vehicles = get_all_vehicles_v2(conn)
    return [v for v in vehicles if isinstance(v, TruckResponseV2)]


@v2_router.post("/trucks", response_model=TruckResponseV2)
async def create_truck_v2(
    truck: TruckCreateV2, conn: sqlite3.Connection = Depends(get_db)
):
    """Create a new truck (V2)."""
    return create_truck_v2(conn, truck)
