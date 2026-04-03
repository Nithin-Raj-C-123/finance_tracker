from sqlalchemy.orm import Session
from datetime import datetime

from app.models.transaction import Transaction


# CREATE
def create_transaction(db: Session, data, user_id: int):
    txn_data = data.model_dump()

    # Handle date (auto if not provided)
    if txn_data.get("date") is None:
        txn_data["date"] = datetime.utcnow()

    txn = Transaction(**txn_data, user_id=user_id)

    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn


# READ + FILTER + PAGINATION
def get_transactions(db: Session, type=None, category=None, skip=0, limit=10):
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.offset(skip).limit(limit).all()


# UPDATE
def update_transaction(db: Session, txn_id: int, data):
    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()

    if not txn:
        return None

    for key, value in data.model_dump().items():
        setattr(txn, key, value)

    db.commit()
    db.refresh(txn)
    return txn


# DELETE
def delete_transaction(db: Session, txn_id: int):
    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()

    if not txn:
        return None

    db.delete(txn)
    db.commit()
    return txn