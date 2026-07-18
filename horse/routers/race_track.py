from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import race_track
from ..oauth2 import get_current_admin, get_admin_or_player

router = APIRouter(
    prefix="/race-tracks",
    tags=["Race Tracks"]
)


@router.post(
    "/",
    response_model=schemas.RaceTrackResponse,
    status_code=status.HTTP_201_CREATED
)
def create_race_track(
    request: schemas.RaceTrackCreate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race_track.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.RaceTrackResponse]
)
def get_all_race_tracks(
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return race_track.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.RaceTrackResponse
)
def get_race_track(
    id: int,
    db: Session = Depends(database.get_db),
    current_user=Depends(get_admin_or_player)
):
    return race_track.get_by_id(id, db)


@router.put(
    "/{id}",
    response_model=schemas.RaceTrackResponse
)
def update_race_track(
    id: int,
    request: schemas.RaceTrackUpdate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race_track.update(id, request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_race_track(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return race_track.delete(id, db)