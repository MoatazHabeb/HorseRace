from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database
from .. import schemas
from ..repository import authentication

router = APIRouter(
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=schemas.Token
)
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
):
    return authentication.login(
        request,
        db
    )