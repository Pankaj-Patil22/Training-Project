from flask import Flask, request, jsonify, session, render_template, flash, redirect, url_for, send_file
#  from flask_cors import CORS
import os, re
import sqlite3

import jsonpickle
from Actions.menu_service_impl import Menu_service_impl as Menu_service

menu_service = Menu_service()

app = Flask(__name__)
# cors = CORS(app)

app.secret_key = os.urandom(24)

#dummy method
@app.route('/getCost/', methods = ['GET'])
# @cross_origin()
def getCost():
    response = jsonify(jsonpickle.encode(123, unpicklable=False))
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

# api end point which get all the menu items
@app.route('/getMenu/', methods = ['GET'])
def getMenu():
    # response = jsonify(jsonpickle.encode(menu_service.get_all_items(), unpicklable=False))
    obidkj = menu_service.get_all_items()
    arr = []
    for obj in obidkj:
        arr.append({
        "item_id": obj.item_id,
        "name": obj.name,
        "description": obj.description,
        "eta": obj.eta,
        "price": obj.price,
        "image": obj.image,
        "rating": obj.rating,
        "veg": obj.veg,
        "serving_size": obj.serving_size
    })
        
    response = jsonify(arr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)