import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/module/<module_id>', methods=['POST'])
def get_module(module_id):
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()
    module = cur.execute('SELECT * FROM Modules where id == ?', (module_id,)).fetchall()
    return jsonify(module)

@app.route('/modules', methods=['POST'])
def get_modules():
    conn = sqlite3.connect('nxbase.sqlite3')
    cur = conn.cursor()
    modules = cur.execute('SELECT * FROM Modules').fetchall()
    return jsonify(modules)


    
app.run()
