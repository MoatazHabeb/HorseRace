from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.RaceCreate, db: Session):

    track = db.query(models.RaceTrack).filter(
        models.RaceTrack.id == request.track_id
    ).first()

    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race track not found."
        )

    race = models.Race(
        name=request.name,
        race_date=request.race_date,
        track_id=request.track_id
    )

    db.add(race)
    db.commit()
    db.refresh(race)

    return race


def get_all(db: Session):

    return db.query(models.Race).all()


def get_by_id(id: int, db: Session):

    race = db.query(models.Race).filter(
        models.Race.id == id
    ).first()

    if race is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race not found."
        )

    return race


def update(id: int, request: schemas.RaceUpdate, db: Session):

    race = db.query(models.Race).filter(
        models.Race.id == id
    )

    if race.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race not found."
        )

    track = db.query(models.RaceTrack).filter(
        models.RaceTrack.id == request.track_id
    ).first()

    if track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race track not found."
        )

    race.update({
        models.Race.name: request.name,
        models.Race.race_date: request.race_date,
        models.Race.status: request.status,
        models.Race.track_id: request.track_id
    })

    db.commit()

    return race.first()


def delete(id: int, db: Session):

    race = db.query(models.Race).filter(
        models.Race.id == id
    )

    if race.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race not found."
        )

    race.delete(synchronize_session=False)
    db.commit()

    return {
        "message": "Race deleted successfully."
    }