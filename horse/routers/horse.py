from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import horse
from ..oauth2 import get_current_admin, get_admin_or_player

router = APIRouter(
    prefix="/horses",
    tags=["Horses"]
)


@router.post(
    "/",
    response_model=schemas.HorseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_horse(
    request: schemas.HorseCreate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return horse.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.HorseResponse]
)
def get_all_horses(
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return horse.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.HorseResponse
)
def get_horse(
    id: int,
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return horse.get_by_id(id, db)


@router.put(
    "/{id}",
    response_model=schemas.HorseResponse
)
def update_horse(
    id: int,
    request: schemas.HorseUpdate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return horse.update(id, request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_horse(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return horse.delete(id, db)