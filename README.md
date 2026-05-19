# Dribbling MVP (Single Stage)

Telegram WebApp платформа для организации любительских футбольных матчей.

## Состав
- `frontend/` — Telegram WebApp (HTML/CSS/JS)
- `backend/` — Python API (Yandex Cloud Functions compatible)
- `admin/` — web-admin панель
- `infra/` — инфраструктурные артефакты (API Gateway/YDB schema)
- `docs/` — API документация

## Быстрый старт локально

### 1) Frontend
```bash
cd frontend
python3 -m http.server 8080
```

### 2) Backend
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 3) Admin
```bash
cd admin
python3 -m http.server 8081
```

## Deploy (Yandex Cloud)
1. Создать YDB и применить `infra/ydb/schema.sql`.
2. Развернуть cloud function из `backend/`.
3. Настроить API Gateway по `infra/apigw/openapi.yaml`.
4. Разместить `frontend/` и `admin/` в Object Storage + CDN.
5. Указать URL WebApp в Telegram BotFather.

## Telegram авторизация
Бэкенд ожидает `initData` и выполняет валидацию подписи Telegram на `/auth`.

## Город MVP
По умолчанию в seed/фильтрах — Пенджикент.
