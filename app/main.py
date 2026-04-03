from fastapi import FastAPI
from app.core.database import Base, engine
from app.api import user_routes, transaction_routes, analytics_routes

app = FastAPI(
    title="Finance Tracker API",
    description="Backend system for managing financial records",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(analytics_routes.router)

# ROOT ROUTE 🔥
@app.get("/")
def root():
    return {"message": "Finance Tracker API is running 🚀"}