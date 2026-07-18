from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def create(request: schemas.BetCreate, current_user, db: Session):

    player = db.query(models.Player).filter(
        models.Player.email == current_user.username
    ).first()

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Player not found."
        )

    horse = db.query(models.Horse).filter(
        models.Horse.id == request.horse_id
    ).first()

    if horse is None:
        raise HTTPException(
            status_code=404,
            detail="Horse not found."
        )

    race = db.query(models.Race).filter(
        models.Race.id == request.race_id
    ).first()

    if race is None:
        raise HTTPException(
            status_code=404,
            detail="Race not found."
        )

    if race.status != "SCHEDULED":
        raise HTTPException(
            status_code=400,
            detail="Betting is closed."
        )

    if player.balance < request.amount:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance."
        )

    player.balance -= request.amount

    bet = models.Bet(
        player_id=player.id,
        horse_id=request.horse_id,
        race_id=request.race_id,
        amount=request.amount,
        odds=2.5
    )

    db.add(bet)

    transaction = models.WalletTransaction(
        player_id=player.id,
        transaction_type="BET",
        amount=request.amount,
        balance_after=player.balance
    )

    db.add(transaction)

    db.commit()

    db.refresh(bet)

    return bet