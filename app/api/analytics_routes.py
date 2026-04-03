from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, require_role
from app.services.analytics_service import (
    get_summary,
    category_breakdown,
    monthly_summary
)

router = APIRouter(prefix="/analytics")

# SUMMARY → ANALYST + ADMIN
@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    user=Depends(require_role("analyst"))
):
    return get_summary(db)

# CATEGORY → ANALYST + ADMIN
@router.get("/category")
def category(
    db: Session = Depends(get_db),
    user=Depends(require_role("analyst"))
):
    return category_breakdown(db)

# MONTHLY → ANALYST + ADMIN
@router.get("/monthly")
def monthly(
    db: Session = Depends(get_db),
    user=Depends(require_role("analyst"))
):
    return monthly_summary(db)