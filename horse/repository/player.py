from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..hashing import Hash


def create(request: schemas.PlayerCreate, db: Session):

    player = db.query(models.Player).filter(
        models.Player.email == request.email
    ).first()

    if player:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists."
        )

    new_player = models.Player(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    return new_player


def get_all(db: Session):
    return db.query(models.Player).all()


def get_by_id(id: int, db: Session):

    player = db.query(models.Player).filter(
        models.Player.id == id
    ).first()

    if not player:
        raise HTTPException(
            status_code=404,
            detail="Player not found."
        )

    return player


def update(id: int, request: schemas.PlayerUpdate, db: Session):

    player = db.query(models.Player).filter(
        models.Player.id == id
    )

    if not player.first():
        raise HTTPException(
            status_code=404,
            detail="Player not found."
        )

    player.update({
        models.Player.name: request.name,
        models.Player.email: request.email
    })

    db.commit()

    return player.first()


def delete(id: int, db: Session):

    player = db.query(models.Player).filter(
        models.Player.id == id
    )

    if not player.first():
        raise HTTPException(
            status_code=404,
            detail="Player not found."
        )

    player.delete(synchronize_session=False)
    db.commit()

    return {
        "message": "Player deleted successfully."
    }