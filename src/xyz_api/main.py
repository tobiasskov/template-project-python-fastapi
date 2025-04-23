from fastapi import FastAPI

from xyz_api.endpoints.vehicles import v1_router, v2_router

app = FastAPI(
    title="XYZ API",
    description="API for managing vehicles, cars, and trucks",
    version="2.0.0",
)

# Include both versioned routers
app.include_router(v1_router)
app.include_router(v2_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "xyz_api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
    )
