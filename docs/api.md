# Dribbling API

## Auth
- `POST /auth` — валидация Telegram `initData`.

## Matches
- `POST /create`
- `GET /all?city=Пенджикент`
- `GET /my`
- `POST /join`
- `POST /leave`
- `POST /remove`

## Profile
- `GET /profile`

## Admin
- `GET /admin/users`
- `GET /admin/matches`
- `POST /admin/block_user?telegram_id=<id>`
- `DELETE /admin/remove_match?match_id=<id>`
