from flask import Flask, request, jsonify, session, render_template, flash, redirect, url_for, send_file
#  from flask_cors import CORS
import os, re
import sqlite3
app = Flask(__name__)
# cors = CORS(app)

app.secret_key = os.urandom(24)

@app.route('/getCost/', methods = ['GET'])
# @cross_origin()
def getCost():
    response = jsonify({"123": 123})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)