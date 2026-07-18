from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import race
from ..oauth2 import get_current_admin, get_admin_or_player

router = APIRouter(
    prefix="/races",
    tags=["Races"]
)


@router.post(
    "/",
    response_model=schemas.RaceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_race(
    request: schemas.RaceCreate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.RaceResponse]
)
def get_all_races(
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return race.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.RaceResponse
)
def get_race(
    id: int,
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return race.get_by_id(id, db)


@router.put(
    "/{id}",
    response_model=schemas.RaceResponse
)
def update_race(
    id: int,
    request: schemas.RaceUpdate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race.update(id, request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_race(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race.delete(id, db)