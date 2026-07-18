from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.RaceTrackCreate, db: Session):

    race_track = models.RaceTrack(
        name=request.name,
        city=request.city,
        capacity=request.capacity
    )

    db.add(race_track)
    db.commit()
    db.refresh(race_track)

    return race_track


def get_all(db: Session):

    return db.query(models.RaceTrack).all()


def get_by_id(id: int, db: Session):

    race_track = db.query(models.RaceTrack).filter(
        models.RaceTrack.id == id
    ).first()

    if not race_track:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race track not found."
        )

    return race_track


def update(id: int, request: schemas.RaceTrackUpdate, db: Session):

    race_track = db.query(models.RaceTrack).filter(
        models.RaceTrack.id == id
    )

    if not race_track.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race track not found."
        )

    race_track.update({
        models.RaceTrack.name: request.name,
        models.RaceTrack.city: request.city,
        models.RaceTrack.capacity: request.capacity
    })

    db.commit()

    return race_track.first()


def delete(id: int, db: Session):

    race_track = db.query(models.RaceTrack).filter(
        models.RaceTrack.id == id
    )

    if not race_track.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race track not found."
        )

    race_track.delete(synchronize_session=False)
    db.commit()

    return {
        "message": "Race track deleted successfully."
    }