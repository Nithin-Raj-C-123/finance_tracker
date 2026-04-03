from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

# ENUM VALIDATION 🔥
class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    amount: float
    type: TransactionType
    category: str
    notes: str
    date: Optional[datetime] = None

class TransactionOut(BaseModel):
    id: int
    amount: float
    type: TransactionType
    category: str
    notes: str
    date: datetime

    class Config:
        from_attributes = True