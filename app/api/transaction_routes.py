from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.transaction_schema import TransactionCreate
from app.crud.transaction_crud import (
    create_transaction,
    get_transactions,
    delete_transaction,
    update_transaction
)
from app.api.deps import get_db, require_role

router = APIRouter(prefix="/transactions")


# CREATE → ADMIN ONLY
@router.post("/")
def create(
    txn: TransactionCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role("admin"))
):
    return create_transaction(db, txn, user_id=1)


# READ → ANALYST + ADMIN + PAGINATION
@router.get("/")
def read(
    type: Optional[str] = None,
    category: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(require_role("analyst"))
):
    return get_transactions(db, type, category, skip, limit)


# UPDATE → ADMIN ONLY
@router.put("/{txn_id}")
def update(
    txn_id: int = Path(...),
    txn: TransactionCreate = ...,
    db: Session = Depends(get_db),
    user=Depends(require_role("admin"))
):
    updated = update_transaction(db, txn_id, txn)

    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return updated


# DELETE → ADMIN ONLY
@router.delete("/{txn_id}")
def delete(
    txn_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role("admin"))
):
    txn = delete_transaction(db, txn_id)

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Deleted successfully"}