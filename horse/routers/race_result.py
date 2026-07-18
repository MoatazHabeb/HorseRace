from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..oauth2 import get_current_admin, get_admin_or_player
from ..repository import race_result

router = APIRouter(
    prefix="/race-results",
    tags=["Race Results"]
)


@router.post(
    "/finish/{race_id}",
    status_code=status.HTTP_200_OK
)
def finish_race(
    race_id: int,
    request: List[schemas.RaceResultCreate],
    db: Session = Depends(database.get_db),
    current_admin: schemas.TokenData = Depends(get_current_admin)
):
    return race_result.finish_race(
        race_id,
        request,
        db
    )


@router.get(
    "/race/{race_id}",
    response_model=List[schemas.RaceResultResponse]
)
def get_results_by_race(
    race_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(get_admin_or_player)
):
    return race_result.get_results_by_race(
        race_id,
        db
    )


@router.get(
    "/{id}",
    response_model=schemas.RaceResultResponse
)
def get_result_by_id(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.TokenData = Depends(get_admin_or_player)
):
    return race_result.get_by_id(
        id,
        db
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_result(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin: schemas.TokenData = Depends(get_current_admin)
):
    return race_result.delete(
        id,
        db
    )