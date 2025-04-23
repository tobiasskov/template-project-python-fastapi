from fastapi import APIRouter

from xyz_api.schemas.vehicles import (
    CarV1,
    CarV2,
    TruckV1,
    TruckV2,
    VehicleV1,
    VehicleV2,
)

# Version 1 router
v1_router = APIRouter(prefix="/api/v1")


@v1_router.get("/vehicles", response_model=list[VehicleV1])
async def get_vehicles_v1():
    """Retrieve a list of vehicles (V1)."""
    return []


@v1_router.post("/vehicles", response_model=VehicleV1)
async def create_vehicle_v1(vehicle: VehicleV1):
    """Create a new vehicle (V1)."""
    return vehicle


@v1_router.get("/cars", response_model=list[CarV1])
async def get_cars_v1():
    """Retrieve a list of cars (V1)."""
    return []


@v1_router.post("/cars", response_model=CarV1)
async def create_car_v1(car: CarV1):
    """Create a new car (V1)."""
    return car


@v1_router.get("/trucks", response_model=list[TruckV1])
async def get_trucks_v1():
    """Retrieve a list of trucks (V1)."""
    return []


@v1_router.post("/trucks", response_model=TruckV1)
async def create_truck_v1(truck: TruckV1):
    """Create a new truck (V1)."""
    return truck


# Version 2 router
v2_router = APIRouter(prefix="/api/v2")


@v2_router.get("/vehicles", response_model=list[VehicleV2])
async def get_vehicles_v2():
    """Retrieve a list of vehicles (V2)."""
    return []


@v2_router.post("/vehicles", response_model=VehicleV2)
async def create_vehicle_v2(vehicle: VehicleV2):
    """Create a new vehicle (V2)."""
    return vehicle


@v2_router.get("/cars", response_model=list[CarV2])
async def get_cars_v2():
    """Retrieve a list of cars (V2)."""
    return []


@v2_router.post("/cars", response_model=CarV2)
async def create_car_v2(car: CarV2):
    """Create a new car (V2)."""
    return car


@v2_router.get("/trucks", response_model=list[TruckV2])
async def get_trucks_v2():
    """Retrieve a list of trucks (V2)."""
    return []


@v2_router.post("/trucks", response_model=TruckV2)
async def create_truck_v2(truck: TruckV2):
    """Create a new truck (V2)."""
    return truck
