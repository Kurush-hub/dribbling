CREATE TABLE users (
    telegram_id Int64,
    username Utf8,
    first_name Utf8,
    photo_url Utf8,
    city Utf8,
    rating Double,
    matches_count Int32,
    position Utf8,
    is_blocked Bool,
    created_at Timestamp,
    PRIMARY KEY (telegram_id)
);

CREATE TABLE matches (
    match_id Utf8,
    creator_id Int64,
    title Utf8,
    city Utf8,
    location Utf8,
    match_date Timestamp,
    game_format Utf8,
    players_limit Int32,
    players_count Int32,
    price Int32,
    players Json,
    status Utf8,
    comment Utf8,
    created_at Timestamp,
    PRIMARY KEY (match_id)
);

CREATE TABLE match_players (
    relation_id Utf8,
    match_id Utf8,
    player_id Int64,
    joined_at Timestamp,
    PRIMARY KEY (relation_id)
);

CREATE TABLE reviews (
    review_id Utf8,
    from_user Int64,
    to_user Int64,
    rating Int32,
    comment Utf8,
    created_at Timestamp,
    PRIMARY KEY (review_id)
);
