import os
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request

from .auth import validate_telegram_init_data
from .models import AuthPayload, JoinLeavePayload, MatchCreate, RemovePayload
from .storage import MATCHES, USERS, create_match

app = FastAPI(title="Dribbling API", version="0.1.0")


@app.post("/auth")
def auth(payload: AuthPayload):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "dev-token")
    if not validate_telegram_init_data(payload.initData, bot_token):
        raise HTTPException(status_code=401, detail="Invalid Telegram initData")
    return {"ok": True}


@app.post("/create")
def create(payload: MatchCreate, request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    return create_match(payload, user_id)


@app.get("/all")
def all_matches(city: str | None = None):
    items = list(MATCHES.values())
    if city:
        items = [m for m in items if m["city"].lower() == city.lower()]
    return items


@app.get("/my")
def my_matches(request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    mine = [m for m in MATCHES.values() if user_id in m["players"]]
    return mine


@app.post("/join")
def join(payload: JoinLeavePayload, request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    match = MATCHES.get(payload.match_id)
    if not match:
        raise HTTPException(404, "Match not found")
    if match["creator_id"] == user_id:
        raise HTTPException(400, "Cannot join own match")
    if user_id in match["players"]:
        raise HTTPException(400, "Already joined")
    if match["players_count"] >= match["players_limit"]:
        raise HTTPException(400, "No places left")
    match["players"].append(user_id)
    match["players_count"] += 1
    return {"ok": True, "players_count": match["players_count"]}


@app.post("/leave")
def leave(payload: JoinLeavePayload, request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    match = MATCHES.get(payload.match_id)
    if not match:
        raise HTTPException(404, "Match not found")
    if user_id not in match["players"]:
        raise HTTPException(400, "Not in match")
    match["players"].remove(user_id)
    match["players_count"] = max(0, match["players_count"] - 1)
    return {"ok": True}


@app.post("/remove")
def remove(payload: RemovePayload, request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    is_admin = request.headers.get("x-admin", "0") == "1"
    match = MATCHES.get(payload.match_id)
    if not match:
        raise HTTPException(404, "Match not found")
    if match["creator_id"] != user_id and not is_admin:
        raise HTTPException(403, "Forbidden")
    del MATCHES[payload.match_id]
    return {"ok": True, "notified": True}


@app.get("/profile")
def profile(request: Request):
    user_id = int(request.headers.get("x-user-id", "1"))
    return USERS.get(user_id, {"telegram_id": user_id, "created_at": datetime.utcnow().isoformat()})


@app.get("/admin/users")
def admin_users():
    return list(USERS.values())


@app.get("/admin/matches")
def admin_matches():
    return list(MATCHES.values())


@app.post("/admin/block_user")
def admin_block_user(request: Request):
    body = request.query_params
    uid = int(body.get("telegram_id", "0"))
    if uid in USERS:
        USERS[uid]["is_blocked"] = True
    return {"ok": True}


@app.delete("/admin/remove_match")
def admin_remove_match(match_id: str):
    MATCHES.pop(match_id, None)
    return {"ok": True}
