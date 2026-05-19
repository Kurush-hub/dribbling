from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


MatchStatus = Literal["active", "completed", "cancelled"]
GameFormat = Literal["5x5", "7x7", "11x11"]


class MatchCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    city: str = Field(default="Пенджикент", min_length=2, max_length=64)
    location: str = Field(min_length=3, max_length=160)
    match_date: datetime
    game_format: GameFormat
    players_limit: int = Field(ge=2, le=30)
    price: int = Field(ge=0, le=500)
    comment: str = Field(default="", max_length=300)


class MatchOut(BaseModel):
    match_id: str
    creator_id: int
    title: str
    city: str
    location: str
    match_date: datetime
    game_format: GameFormat
    players_limit: int
    players_count: int
    price: int
    players: list[int]
    status: MatchStatus
    comment: str
    created_at: datetime


class JoinLeavePayload(BaseModel):
    match_id: str


class RemovePayload(BaseModel):
    match_id: str


class AuthPayload(BaseModel):
    initData: str
