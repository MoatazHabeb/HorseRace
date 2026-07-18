from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.HorseCreate, db: Session):

    owner = db.query(models.Owner).filter(
        models.Owner.id == request.owner_id
    ).first()

    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found."
        )

    horse = models.Horse(
        name=request.name,
        age=request.age,
        breed=request.breed,
        speed=request.speed,
        owner_id=request.owner_id
    )

    db.add(horse)
    db.commit()
    db.refresh(horse)

    return horse


def get_all(db: Session):

    return db.query(models.Horse).all()


def get_by_id(id: int, db: Session):

    horse = db.query(models.Horse).filter(
        models.Horse.id == id
    ).first()

    if horse is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Horse not found."
        )

    return horse


def update(id: int, request: schemas.HorseUpdate, db: Session):

    horse = db.query(models.Horse).filter(
        models.Horse.id == id
    )

    if horse.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Horse not found."
        )

    owner = db.query(models.Owner).filter(
        models.Owner.id == request.owner_id
    ).first()

    if owner is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found."
        )

    horse.update({
        models.Horse.name: request.name,
        models.Horse.age: request.age,
        models.Horse.breed: request.breed,
        models.Horse.speed: request.speed,
        models.Horse.status: request.status,
        models.Horse.owner_id: request.owner_id
    })

    db.commit()

    return horse.first()


def delete(id: int, db: Session):

    horse = db.query(models.Horse).filter(
        models.Horse.id == id
    )

    if horse.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Horse not found."
        )

    horse.delete(synchronize_session=False)
    db.commit()

    return {
        "message": "Horse deleted successfully."
    }