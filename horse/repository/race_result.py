from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def finish_race(
        race_id: int,
        request: list[schemas.RaceResultCreate],
        db: Session
):

    race = db.query(models.Race).filter(
        models.Race.id == race_id
    ).first()

    if race is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Race not found."
        )

    if race.status == "FINISHED":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Race already finished."
        )

    if not request:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Race results cannot be empty."
        )

    existing_results = db.query(models.RaceResult).filter(
        models.RaceResult.race_id == race_id
    ).first()

    if existing_results:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Race results already exist."
        )

    positions = set()
    horse_ids = set()
    winner = None

    for item in request:

        if item.position in positions:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Position {item.position} is duplicated."
            )

        positions.add(item.position)

        if item.horse_id in horse_ids:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Horse {item.horse_id} is duplicated."
            )

        horse_ids.add(item.horse_id)

        horse = db.query(models.Horse).filter(
            models.Horse.id == item.horse_id
        ).first()

        if horse is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Horse {item.horse_id} not found."
            )

        result = models.RaceResult(
            race_id=race.id,
            horse_id=item.horse_id,
            position=item.position,
            finish_time=item.finish_time
        )

        db.add(result)

        if item.position == 1:
            winner = horse

    if winner is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There must be one winner."
        )

    winner.wins += 1

    bets = db.query(models.Bet).filter(
        models.Bet.race_id == race.id
    ).all()

    for bet in bets:

        player = db.query(models.Player).filter(
            models.Player.id == bet.player_id
        ).first()

        if bet.horse_id == winner.id:

            bet.status = "WON"

            bet.profit = bet.amount * bet.odds

            player.balance += bet.profit

            transaction = models.WalletTransaction(
                player_id=player.id,
                transaction_type="WIN",
                amount=bet.profit,
                balance_after=player.balance
            )

            db.add(transaction)

        else:

            bet.status = "LOST"
            bet.profit = 0

    race.status = "FINISHED"

    try:
        db.commit()

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to finish race."
        )

    return {
        "message": "Race finished successfully."
    }