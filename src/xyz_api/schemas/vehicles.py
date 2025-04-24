from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class FuelType(Enum):
    GASOLINE = "gasoline"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"


class TransmissionType(Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    CVT = "cvt"


# Version 1 Schemas
class VehicleBaseV1(BaseModel):
    """Base vehicle schema with common fields (V1)."""

    make: str = Field(description="Make of the vehicle")
    model: str = Field(description="Model of the vehicle")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the vehicle")
    vin: str = Field(
        min_length=17, max_length=17, description="Vehicle Identification Number (VIN)"
    )
    mileage: float = Field(ge=0.0, description="Current mileage of the vehicle")
    last_service_date: Optional[date] = Field(None, description="Date of last service")


class VehicleResponseV1(VehicleBaseV1):
    """Base response schema including ID (V1)."""

    id: UUID = Field(description="Unique identifier for the vehicle")


class CarCreateV1(VehicleBaseV1):
    """Schema for creating a car (V1)."""

    doors: int = Field(ge=2, le=5, description="Number of doors")
    trunk_capacity: float = Field(
        ge=0.0, le=100.0, description="Trunk capacity in cubic feet"
    )
    fuel_type: FuelType = Field(description="Type of fuel used")
    transmission: TransmissionType = Field(description="Type of transmission")


class CarResponseV1(CarCreateV1, VehicleResponseV1):
    """Schema for car responses, including ID (V1)."""

    pass


class TruckCreateV1(VehicleBaseV1):
    """Schema for creating a truck (V1)."""

    bed_length: float = Field(gt=0.0, description="Length of the truck bed in feet")
    towing_capacity: float = Field(
        ge=0.0, le=100000.0, description="Towing capacity in pounds"
    )
    payload_capacity: float = Field(
        gt=0.0, description="Maximum payload capacity in pounds"
    )
    engine_size: float = Field(gt=0.0, description="Engine size in liters")


class TruckResponseV1(TruckCreateV1, VehicleResponseV1):
    """Schema for truck responses, including ID (V1)."""

    pass


# Version 2 Schemas
class VehicleBaseV2(BaseModel):
    """Base vehicle schema with common fields (V2)."""

    make: str = Field(description="Make of the vehicle")
    model: str = Field(description="Model of the vehicle")
    year: int = Field(description="Year of manufacture")
    color: str = Field(description="Color of the vehicle")
    vin: str = Field(
        min_length=17, max_length=17, description="Vehicle Identification Number (VIN)"
    )
    # Removed mileage and last_service_date from base
    # Added new fields
    registration_number: str = Field(description="Vehicle registration number")
    insurance_expiry: Optional[date] = Field(None, description="Insurance expiry date")
    is_available: bool = Field(
        default=True, description="Whether the vehicle is available for use"
    )


class VehicleResponseV2(VehicleBaseV2):
    """Base response schema including ID (V2)."""

    id: UUID = Field(description="Unique identifier for the vehicle")
    mileage: float = Field(ge=0.0, description="Current mileage of the vehicle")
    last_service_date: Optional[date] = Field(None, description="Date of last service")


class CarCreateV2(VehicleBaseV2):
    """Schema for creating a car (V2)."""

    doors: int = Field(ge=2, le=5, description="Number of doors")
    trunk_capacity: float = Field(
        ge=0.0, le=100.0, description="Trunk capacity in cubic feet"
    )
    fuel_type: FuelType = Field(description="Type of fuel used")
    transmission: TransmissionType = Field(description="Type of transmission")
    # Added new fields
    sunroof: bool = Field(default=False, description="Whether the car has a sunroof")
    parking_sensors: bool = Field(
        default=False, description="Whether the car has parking sensors"
    )


class CarResponseV2(CarCreateV2, VehicleResponseV2):
    """Schema for car responses, including ID (V2)."""

    pass


class TruckCreateV2(VehicleBaseV2):
    """Schema for creating a truck (V2)."""

    bed_length: float = Field(gt=0.0, description="Length of the truck bed in feet")
    towing_capacity: float = Field(
        ge=0.0, le=100000.0, description="Towing capacity in pounds"
    )
    payload_capacity: float = Field(
        gt=0.0, description="Maximum payload capacity in pounds"
    )
    engine_size: float = Field(gt=0.0, description="Engine size in liters")
    # Added new fields
    four_wheel_drive: bool = Field(
        default=False, description="Whether the truck has four-wheel drive"
    )
    bed_liner: bool = Field(
        default=False, description="Whether the truck has a bed liner"
    )


class TruckResponseV2(TruckCreateV2, VehicleResponseV2):
    """Schema for truck responses, including ID (V2)."""

    pass
