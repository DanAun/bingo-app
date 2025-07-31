from flask import Flask, render_template, request, jsonify, g
import sqlite3
import json
import os

app = Flask(__name__)
DATABASE = 'database/db.sqlite3'

# --- DATABASE HANDLING ---

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql') as f:
            db.executescript(f.read())
        # Load bingo card
        with open('bingo_data.json') as f:
            cells = json.dumps(json.load(f))
        db.execute("INSERT INTO bingo_card (cells) VALUES (?)", (cells,))
        db.commit()

if not os.path.exists(DATABASE):
    init_db()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/player/<name>')
def bingo_card(name):
    db = get_db()
    db.execute("INSERT OR IGNORE INTO players (name) VALUES (?)", (name,))
    card_row = db.execute("SELECT cells FROM bingo_card LIMIT 1").fetchone()
    card = json.loads(card_row['cells'])
    marks = db.execute("SELECT cell_index FROM marked_cells WHERE player_name = ?", (name,)).fetchall()
    marked = [r['cell_index'] for r in marks]
    return render_template("bingo.html", name=name, card=card, marked=marked)

@app.route('/<name>/mark', methods=["POST"])
def mark_cell(name):
    data = request.get_json()
    index = int(data['cell_index'])
    db = get_db()
    db.execute("INSERT OR IGNORE INTO marked_cells (player_name, cell_index) VALUES (?, ?)", (name, index))
    db.commit()
    return jsonify({"status": "ok"})

@app.route('/<name>/unmark', methods=["POST"])
def unmark_cell(name):
    data = request.get_json()
    index = int(data['cell_index'])
    db = get_db()
    db.execute("DELETE FROM marked_cells WHERE player_name = ? AND cell_index = ?", (name, index))
    db.commit()
    return jsonify({"status": "ok"})
