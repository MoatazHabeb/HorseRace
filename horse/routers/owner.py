from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import owner
from ..oauth2 import get_current_admin,get_admin_or_player

router = APIRouter(
    prefix="/owners",
    tags=["Owners"]
)


@router.post(
    "/",
    response_model=schemas.OwnerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_owner(
    request: schemas.OwnerCreate,
    db: Session = Depends(database.get_db),
        current_admin=Depends(get_current_admin)):
    return owner.create(request, db)


@router.get(
    "/",
    response_model=List[schemas.OwnerResponse]
)
def get_all_owners(
    db: Session = Depends(database.get_db)
):
    return owner.get_all(db)


@router.get(
    "/{id}",
    response_model=schemas.OwnerResponse
)
def get_owner(
    id: int,
    db: Session = Depends(database.get_db)
):
    return owner.get_by_id(id, db)


@router.put(
    "/{id}",
    response_model=schemas.OwnerResponse
)
def update_owner(
    id: int,
    request: schemas.OwnerUpdate,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return owner.update(id, request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK
)
def delete_owner(
    id: int,
    db: Session = Depends(database.get_db),
    current_admin=Depends(get_current_admin)
):
    return owner.delete(id, db)