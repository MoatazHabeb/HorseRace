from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.OwnerCreate, db: Session):

    owner = models.Owner(
        name=request.name,
        country=request.country
    )

    db.add(owner)
    db.commit()
    db.refresh(owner)

    return owner


def get_all(db: Session):

    return db.query(models.Owner).all()


def get_by_id(id: int, db: Session):

    owner = db.query(models.Owner).filter(
        models.Owner.id == id
    ).first()

    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found."
        )

    return owner


def update(id: int, request: schemas.OwnerUpdate, db: Session):

    owner = db.query(models.Owner).filter(
        models.Owner.id == id
    )

    if not owner.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found."
        )

    owner.update({
        models.Owner.name: request.name,
        models.Owner.country: request.country
    })

    db.commit()

    return owner.first()


def delete(id: int, db: Session):

    owner = db.query(models.Owner).filter(
        models.Owner.id == id
    )

    if not owner.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found."
        )

    owner.delete(synchronize_session=False)
    db.commit()

    return {
        "message": "Owner deleted successfully."
    }