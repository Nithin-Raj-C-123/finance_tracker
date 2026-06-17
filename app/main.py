from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.transaction_routes import router as transaction_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transaction_router)

@app.get("/")
def root():
    return {"message": "Finance Tracker API Running"}