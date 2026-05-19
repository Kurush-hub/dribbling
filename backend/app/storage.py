from datetime import datetime
from uuid import uuid4

from .models import MatchCreate

USERS = {
    1: {
        "telegram_id": 1,
        "username": "demo_player",
        "first_name": "Demo",
        "city": "Пенджикент",
        "rating": 4.8,
        "matches_count": 12,
        "position": "CM",
        "is_blocked": False,
        "created_at": datetime.utcnow().isoformat(),
    }
}
MATCHES: dict[str, dict] = {}


def create_match(payload: MatchCreate, creator_id: int) -> dict:
    match_id = str(uuid4())
    rec = {
        "match_id": match_id,
        "creator_id": creator_id,
        "title": payload.title,
        "city": payload.city,
        "location": payload.location,
        "match_date": payload.match_date,
        "game_format": payload.game_format,
        "players_limit": payload.players_limit,
        "players_count": 1,
        "price": payload.price,
        "players": [creator_id],
        "status": "active",
        "comment": payload.comment,
        "created_at": datetime.utcnow(),
    }
    MATCHES[match_id] = rec
    return rec
