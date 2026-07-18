from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from .. import jwt_handler
from ..hashing import Hash


def login(request, db: Session):

    player = db.query(models.Player).filter(
        models.Player.email == request.username
    ).first()

    if player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Email"
        )

    if not Hash.verify(player.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Password"
        )

    access_token = jwt_handler.create_access_token(
        data={
            "sub": player.email,
            "role": player.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }