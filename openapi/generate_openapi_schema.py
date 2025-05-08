import json
import os

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from xyz_api.endpoints.vehicles import v1_router, v2_router


# Generate the OpenAPI schema
def generate_openapi_schema():
    app = FastAPI(
        title="XYZ API",
        description="API for managing vehicles, cars, and trucks",
        version="2.0.0",
    )

    # Include both versioned routers
    app.include_router(v1_router)
    app.include_router(v2_router)

    openapi_schema = get_openapi(
        title="System Designer Schemas",
        version="1.0.0",
        description="JSON schemas for the System Designer project",
        routes=app.routes,
    )

    # Create directory if it doesn't exist
    os.makedirs("openapi", exist_ok=True)

    # Write the schema to a file
    with open("openapi/openapi.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)

    print("OpenAPI schema generated at openapi/openapi.json")


if __name__ == "__main__":
    generate_openapi_schema()
