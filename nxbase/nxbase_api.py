import flask
from flask import request, jsonify
import sqlite3
import time

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


app.run()
