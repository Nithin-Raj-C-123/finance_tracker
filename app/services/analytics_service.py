from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from sqlalchemy import func, extract

# SUMMARY
def get_summary(db: Session):
    income = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "income").scalar() or 0
    expense = db.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense").scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }

# CATEGORY
def category_breakdown(db: Session):
    data = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    return [{"category": c, "total": t} for c, t in data]

# MONTHLY (NEW 🔥)
def monthly_summary(db: Session):
    data = db.query(
        extract('month', Transaction.date),
        func.sum(Transaction.amount)
    ).group_by(extract('month', Transaction.date)).all()

    return [{"month": int(m), "total": t} for m, t in data]