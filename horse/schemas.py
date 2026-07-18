from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

         #Player
class PlayerCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class PlayerUpdate(BaseModel):
    name: str
    email: EmailStr


class PlayerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    balance: float
    role: str
    created_at: datetime

    class Config:
        from_attributes = True



         # Login
class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    role: str




       #Owner
class OwnerCreate(BaseModel):
    name: str
    country: str


class OwnerUpdate(BaseModel):
    name: str
    country: str


class OwnerResponse(BaseModel):
    id: int
    name: str
    country: str

    class Config:
        from_attributes = True



        #RaceTrack
class RaceTrackCreate(BaseModel):
    name: str
    city: str
    capacity: int


class RaceTrackUpdate(BaseModel):
    name: str
    city: str
    capacity: int


class RaceTrackResponse(BaseModel):
    id: int
    name: str
    city: str
    capacity: int

    class Config:
        from_attributes = True


      #Horse
class HorseCreate(BaseModel):
    name: str
    age: int
    breed: str
    speed: float
    owner_id: int


class HorseUpdate(BaseModel):
    name: str
    age: int
    breed: str
    speed: float
    status: str
    owner_id: int


class HorseResponse(BaseModel):
    id: int
    name: str
    age: int
    breed: str
    speed: float
    wins: int
    status: str
    owner_id: int

    class Config:
        from_attributes = True



   #Race
class RaceCreate(BaseModel):
    name: str
    race_date: datetime
    track_id: int


class RaceUpdate(BaseModel):
    name: str
    race_date: datetime
    status: str
    track_id: int


class RaceResponse(BaseModel):
    id: int
    name: str
    race_date: datetime
    status: str
    track_id: int

    class Config:
        from_attributes = True



    #Bet
class BetCreate(BaseModel):
    horse_id: int
    race_id: int
    amount: float


class BetResponse(BaseModel):
    id: int
    player_id: int
    horse_id: int
    race_id: int
    amount: float
    odds: float
    status: str
    profit: float
    created_at: datetime

    class Config:
        from_attributes = True



       #RaceResult
class RaceResultItem(BaseModel):
    horse_id: int
    position: int
    finish_time: float

class RaceResultCreate(BaseModel):
    horse_id: int
    position: int
    finish_time: float


class RaceResultResponse(BaseModel):
    id: int
    race_id: int
    horse_id: int
    position: int
    finish_time: float

    class Config:
        from_attributes = True


        #WalletTransaction
class WalletTransactionResponse(BaseModel):
    id: int
    player_id: int
    transaction_type: str
    amount: float
    balance_after: float
    created_at: datetime

    class Config:
        from_attributes = True