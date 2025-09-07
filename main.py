from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import reports, geospatial, statistics

app = FastAPI(title="Ocean Hazard Reporter API", version="1.0.0")

# CORS middleware - must be added before routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(geospatial.router, prefix="/api/geospatial", tags=["geospatial"])
app.include_router(statistics.router, prefix="/api/statistics", tags=["statistics"])

@app.get("/")
async def root():
    return {"message": "Ocean Hazard Reporter API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)