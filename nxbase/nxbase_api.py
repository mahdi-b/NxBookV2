import flask
from flask import request, jsonify
import sqlite3
import time
from datetime import date
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/module/<module_id>', methods=['POST'])
def get_module(module_id):
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()
    module = cur.execute('SELECT * FROM Modules where id = ?', (module_id,)).fetchall()
    return jsonify(module)

@app.route('/modules', methods=['POST'])
def get_modules():
    # time.sleep(2)
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()
    modules = cur.execute('SELECT * FROM Modules').fetchall()
    resp = jsonify(modules)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/questions/<module_id>', methods=['POST'])
def get_questions(module_id):
    time.sleep(2)
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()
    modules = cur.execute('SELECT * FROM Questions where module_id = ?', (module_id,)).fetchall()
    resp = jsonify(modules)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

# add a new article
@app.route('/questions/', methods=['PUT'])
def add_question():
    question = json.loads(request.data)
    data = (
                question["module_id"],
                question["title"],
                question["text"],
                question["type"],
                str(date.today())
            )
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()

    # add question to the
    sql = """INSERT INTO Questions ( module_id, short_text, details, type, date_added) VALUES (?, ?, ?, ?, ?)"""
    cur.execute(sql, data)
    question_id = cur.lastrowid

    # add answers
    sql = """INSERT INTO Answers (text, correct, explanation, question_id) VALUES (?, ?, ?, ?) """
    for q in question["answers"]:
        data = ( q["answer"], q["correct"], q["explanation"], question_id)
        cur.execute(sql, data)

    # add hints
    sql = """INSERT INTO Hints(text, question_id) VALUES (?, ?) """
    for h in question["hints"]:
        cur.execute(sql, (h["text"], question_id))

    conn.commit()

    resp = jsonify({"status": "Completed"})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp




app.run()
