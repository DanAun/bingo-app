-- Run this once to set up the database
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS marked_cells;
DROP TABLE IF EXISTS bingo_card;

CREATE TABLE players (
    name TEXT PRIMARY KEY
);

CREATE TABLE bingo_card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cells TEXT  -- JSON encoded list of 25 strings
);

CREATE TABLE marked_cells (
    player_name TEXT,
    cell_index INTEGER,
    PRIMARY KEY (player_name, cell_index),
    FOREIGN KEY (player_name) REFERENCES players(name)
);
