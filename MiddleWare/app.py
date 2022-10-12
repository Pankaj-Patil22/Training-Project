from flask import Flask, jsonify
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
@app.route('/Tables', methods = ['GET'])
def get_available_tables():
    date=Date(2019, 12, 2)
    reservation=TableService.get_available_tables(2,date )[0]
    table_reservation=available_table_dto.AvailableTableDTO(reservation).__dict__
    response = jsonify({"table_reservation": table_reservation})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)