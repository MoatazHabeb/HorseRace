from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models


def get_my_transactions(current_user, db: Session):

    player = db.query(models.Player).filter(
        models.Player.email == current_user.username
    ).first()

    if player is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found."
        )

    return db.query(models.WalletTransaction).filter(
        models.WalletTransaction.player_id == player.id
    ).order_by(
        models.WalletTransaction.created_at.desc()
    ).all()


def get_all(db: Session):

    return db.query(models.WalletTransaction).order_by(
        models.WalletTransaction.created_at.desc()
    ).all()


def get_by_id(id: int, db: Session):

    transaction = db.query(models.WalletTransaction).filter(
        models.WalletTransaction.id == id
    ).first()

    if transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found."
        )

    return transaction