from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Identity,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    balance = Column(Float, default=0)
    role = Column(String(20), default="PLAYER")
    created_at = Column(DateTime, default=datetime.utcnow)

    bets = relationship("Bet", back_populates="player")
    transactions = relationship("WalletTransaction", back_populates="player")


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100))

    horses = relationship("Horse", back_populates="owner")


class RaceTrack(Base):
    __tablename__ = "race_tracks"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100))
    capacity = Column(Integer)

    races = relationship("Race", back_populates="track")


class Horse(Base):
    __tablename__ = "horses"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    breed = Column(String(100))
    speed = Column(Float)
    wins = Column(Integer, default=0)
    status = Column(String(30), default="ACTIVE")

    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner = relationship("Owner", back_populates="horses")
    bets = relationship("Bet", back_populates="horse")
    results = relationship("RaceResult", back_populates="horse")


class Race(Base):
    __tablename__ = "races"

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(100), nullable=False)
    race_date = Column(DateTime)
    status = Column(String(30), default="SCHEDULED")

    track_id = Column(Integer, ForeignKey("race_tracks.id"))

    track = relationship("RaceTrack", back_populates="races")
    bets = relationship("Bet", back_populates="race")
    results = relationship("RaceResult", back_populates="race")


class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, Identity(start=1), primary_key=True)

    player_id = Column(Integer, ForeignKey("players.id"))
    horse_id = Column(Integer, ForeignKey("horses.id"))
    race_id = Column(Integer, ForeignKey("races.id"))

    amount = Column(Float, nullable=False)
    odds = Column(Float, nullable=False)

    status = Column(String(20), default="PENDING")
    profit = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player", back_populates="bets")
    horse = relationship("Horse", back_populates="bets")
    race = relationship("Race", back_populates="bets")


class RaceResult(Base):
    __tablename__ = "race_results"

    id = Column(Integer, Identity(start=1), primary_key=True)

    race_id = Column(Integer, ForeignKey("races.id"))
    horse_id = Column(Integer, ForeignKey("horses.id"))

    position = Column(Integer)
    finish_time = Column(Float)

    race = relationship("Race", back_populates="results")
    horse = relationship("Horse", back_populates="results")


class WalletTransaction(Base):
    __tablename__ = "wallet_transactions"

    id = Column(Integer, Identity(start=1), primary_key=True)

    player_id = Column(Integer, ForeignKey("players.id"))

    transaction_type = Column(String(30))
    amount = Column(Float)
    balance_after = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)

    player = relationship("Player", back_populates="transactions")