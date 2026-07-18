from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database, schemas
from ..oauth2 import get_current_admin, get_current_user
from ..repository import wallet

router = APIRouter(
    prefix="/wallet",
    tags=["Wallet"]
)


@router.get(
    "/",
    response_model=List[schemas.WalletTransactionResponse]
)
def my_transactions(
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(get_current_user)
):
    return wallet.get_my_transactions(
        current_user,
        db
    )


@router.get(
    "/all",
    response_model=List[schemas.WalletTransactionResponse]
)
def get_all_transactions(
    db: Session = Depends(database.get_db),
    current_admin: schemas.TokenData = Depends(get_current_admin)
):
    return wallet.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.WalletTransactionResponse
)
def get_transaction(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin: schemas.TokenData = Depends(get_current_admin)
):
    return wallet.get_by_id(
        id,
        db
    )