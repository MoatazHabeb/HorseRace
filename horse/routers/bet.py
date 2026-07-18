from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database
from .. import schemas
from ..oauth2 import get_current_user
from ..repository import bet

router = APIRouter(
    prefix="/bets",
    tags=["Bets"]
)


@router.post(
    "/",
    response_model=schemas.BetResponse,
    status_code=status.HTTP_201_CREATED
)
def create_bet(
    request: schemas.BetCreate,
    db: Session = Depends(database.get_db),
    current_user=Depends(get_current_user)
):
    return bet.create(
        request,
        current_user,
        db
    )