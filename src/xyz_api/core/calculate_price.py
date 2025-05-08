from datetime import datetime

from xyz_api.schemas.vehicles import VehicleBaseV1


def calculate_expected_price(vehicle: VehicleBaseV1) -> float:
    current_year = datetime.now().year

    vehicle_age = current_year - vehicle.year

    # If car is from 2025 this will return division by zero error (which needs to be caught in testing):
    print(f"Vehicle mileage: {vehicle.mileage}, vehicle age: {vehicle_age}")
    return vehicle.mileage / vehicle_age
