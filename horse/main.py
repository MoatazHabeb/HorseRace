from fastapi import FastAPI
from . import models
from .database import engine, SessionLocal
from .routers import player,authentication,owner,race_track,horse,race,race_result,wallet,bet
app = FastAPI()








models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)
app.include_router(player.router)
app.include_router(owner.router)

app.include_router(race_track.router)

app.include_router(horse.router)

app.include_router(race.router)

app.include_router(bet.router)

app.include_router(race_result.router)

app.include_router(wallet.router)

