from typing import Optional

from pydantic import BaseModel, Field


# Version 1 Schemas
class VehicleV1(BaseModel):
    """Vehicle schema version 1."""

    id: int = Field(description="Unique identifier for the vehicle")
    make: str = Field(description="Make of the vehicle")
    model: str = Field(description="Model of the vehicle")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the vehicle")
    vin: str = Field(description="Vehicle Identification Number (VIN)")


class CarV1(VehicleV1):
    """Car schema version 1, inheriting from VehicleV1."""

    doors: int = Field(description="Number of doors")
    trunk_capacity: float = Field(
        ge=0.0, le=100.0, description="Trunk capacity in cubic feet"
    )


class TruckV1(VehicleV1):
    """Truck schema version 1, inheriting from VehicleV1."""

    bed_length: float = Field(description="Length of the truck bed in feet")
    towing_capacity: float = Field(
        ge=0.0, le=1000.0, description="Towing capacity in pounds"
    )


# Version 2 Schemas (Separate models approach)
class VehicleV2(BaseModel):
    """Vehicle schema version 2."""

    id: int = Field(description="Unique identifier for the vehicle")
    make: str = Field(description="Make of the vehicle")
    model: str = Field(description="Model of the vehicle")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the vehicle")
    vin: str = Field(description="Vehicle Identification Number (VIN)")
    # New fields in V2
    mileage: float = Field(ge=0.0, description="Current mileage of the vehicle")
    last_service_date: Optional[str] = Field(None, description="Date of last service")


class CarV2(BaseModel):
    """Car schema version 2."""

    id: int = Field(description="Unique identifier for the car")
    make: str = Field(description="Make of the car")
    model: str = Field(description="Model of the car")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the car")
    vin: str = Field(description="Vehicle Identification Number (VIN)")
    mileage: float = Field(ge=0.0, description="Current mileage of the car")
    last_service_date: Optional[str] = Field(None, description="Date of last service")
    # Car-specific fields
    doors: int = Field(description="Number of doors")
    trunk_capacity: float = Field(
        ge=0.0, le=100.0, description="Trunk capacity in cubic feet"
    )
    fuel_type: str = Field(description="Type of fuel used")
    transmission: str = Field(description="Type of transmission")


class TruckV2(BaseModel):
    """Truck schema version 2."""

    id: int = Field(description="Unique identifier for the truck")
    make: str = Field(description="Make of the truck")
    model: str = Field(description="Model of the truck")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the truck")
    vin: str = Field(description="Vehicle Identification Number (VIN)")
    mileage: float = Field(ge=0.0, description="Current mileage of the truck")
    last_service_date: Optional[str] = Field(None, description="Date of last service")
    # Truck-specific fields
    bed_length: float = Field(description="Length of the truck bed in feet")
    towing_capacity: float = Field(
        ge=0.0, le=1000.0, description="Towing capacity in pounds"
    )
    payload_capacity: float = Field(
        ge=0.0, description="Maximum payload capacity in pounds"
    )
    engine_size: float = Field(description="Engine size in liters")
