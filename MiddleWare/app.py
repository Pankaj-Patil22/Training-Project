from flask import Flask, jsonify,request
#  from flask_cors import CORS
import os

import jsonpickle
from Actions.menu_service_impl import Menu_service_impl as Menu_service

menu_service = Menu_service()
import os
from sqlite3 import Date
import DTO.available_table_dto as available_table_dto
from Actions.table_service_impl import TableServiceImpl as TableService

table_service = TableService()

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
@app.route('/tables/<int:year>/<int:month>/<int:day>/<int:time_slot_id>', methods = ['GET'])
def get_available_tables(year, month, day, time_slot_id):
    if request.method == 'GET':
        date=Date(year,month,day)
        table_reservation=TableService.get_available_tables(time_slot_id,date )
        response = jsonify({"table_reservation": table_reservation})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/tables/booking', methods = ['POST'])
def insert_table_reservation():
    if request.method == 'POST':
        date=Date(request.json['date']['year'],request.json['date']['month'],request.json['date']['day'])
        time_slot_id=request.json['time_slot_id']
        reservations=request.json['reservations']
        TableService.insert_table_reservations(date,time_slot_id,reservations)
        response = jsonify({"message": "success"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/tables/price', methods = ['GET'])
def get_price():
    if request.method == 'GET':
        price=[1000,500,500,1000,1000,500,500,1000,1000,500,500,1000]
        response = jsonify({"prices": price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)