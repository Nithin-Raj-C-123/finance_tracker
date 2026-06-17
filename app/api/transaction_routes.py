from fastapi import APIRouter
from app.schemas.transaction_schema import TransactionCreate
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

transactions = []
current_id = 1


@router.get("/")
def get_transactions():

    logger.info("GET - Fetching Transactions")

    return transactions


@router.post("/")
def create_transaction(transaction: TransactionCreate):

    global current_id

    data = {
        "id": current_id,
        **transaction.model_dump()
    }

    transactions.append(data)

    logger.info(
        f"POST - Transaction Created: {transaction.category}"
    )

    current_id += 1

    return data


@router.put("/{txn_id}")
def update_transaction(
    txn_id: int,
    transaction: TransactionCreate
):

    for txn in transactions:

        if txn["id"] == txn_id:

            txn.update(
                transaction.model_dump()
            )

            logger.info(
                f"PUT - Transaction Updated ID={txn_id}"
            )

            return txn

    return {"message": "Not Found"}


@router.delete("/{txn_id}")
def delete_transaction(txn_id: int):

    global transactions

    transactions = [
        t for t in transactions
        if t["id"] != txn_id
    ]

    logger.info(
        f"DELETE - Transaction Deleted ID={txn_id}"
    )

    return {
        "message": "Deleted Successfully"
    }