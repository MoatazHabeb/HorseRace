from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database
from .. import schemas
from ..repository import player

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


@router.post(
    "/",
    response_model=schemas.PlayerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_player(
    request: schemas.PlayerCreate,
    db: Session = Depends(database.get_db)
):
    return player.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.PlayerResponse]
)
def get_players(
    db: Session = Depends(database.get_db)
):
    return player.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.PlayerResponse
)
def get_player(
    id: int,
    db: Session = Depends(database.get_db)
):
    return player.get_by_id(id, db)


@router.put(
    "/{id}",
    response_model=schemas.PlayerResponse
)
def update_player(
    id: int,
    request: schemas.PlayerUpdate,
    db: Session = Depends(database.get_db)
):
    return player.update(id, request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_player(
    id: int,
    db: Session = Depends(database.get_db)
):
    return player.delete(id, db)