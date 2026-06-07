from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

# Create the FastAPI application instance.
# This object is the core of everything — routers, middleware,
# and event handlers all attach to it.
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered clinical document analysis API",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware — controls which domains can call this API.
# During development we allow everything ("*").
# In production this would be locked to specific domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint.
# This is the first real endpoint of our API.
# It tells anyone (including deployment platforms) that the app is alive.
@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }


# Root endpoint — useful for quick sanity checks.
@app.get("/", tags=["System"])
async def root():
    return {
        "message": "Welcome to the Clinical Document Intelligence API",
        "docs": "/docs",
    }