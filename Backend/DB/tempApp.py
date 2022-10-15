# edited app.py file 
from flask import Flask, request, jsonify, session, render_template, flash, redirect, url_for, send_file
from flask_cors import CORS
import os, jsonpickle
from Actions.menu_service_impl import Menu_service_impl as Menu_service
from sqlite3 import Date
import DTO.available_table_dto as available_table_dto
from Actions.table_service_impl import TableServiceImpl as TableService
    
class Server:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.secret_key = os.urandom(24)
        self.table_service = TableService()
        self.menu_service = Menu_service()
        
        @self.app.route('/getTableSessions/', methods = ['GET'])
        def __table_Sessions():
            return self.get_table_sessions()

        @self.app.route('/getTablePrices/', methods = ['GET'])
        def __table_Price():
            return self.get_table_prices()

        @self.app.route('/transactionData/', methods=['POST'])
        def __transaction_data():
            return self.post_transaction_data()

        @self.app.route('/Tables/', methods = ['GET'])
        def __available_tables():
            return self.get_available_tables()
        
        @self.app.route('/getMenu/', methods = ['GET'])
        def __menu():
            return self.getMenu()
    
    def getApp(self):
        return self.app
    
    def getMenu(self):
        all_items = self.menu_service.get_all_items()
        arr = []
        for item in all_items:
           arr.append({
           "item_id": item.item_id,
           "name": item.name,
           "description": item.description,
           "eta": item.eta,
           "price": item.price,
           "image": item.image,
           "rating": item.rating,
           "veg": item.veg,
           "serving_size": item.serving_size})
        response = jsonify(arr)
        return response       
        
    def get_available_tables(self):
        date=Date(2019, 12, 2)
        reservation=TableService.get_available_tables(2,date )[0]
        table_reservation=available_table_dto.AvailableTableDTO(reservation).__dict__
        response = jsonify({"table_reservation": table_reservation})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def get_table_sessions(self):
        tableSessions = {
            1:"8-9",
            2:"9-10",
            3:"10-11",
            4:"11-12",
            5:"12-13",
            6:"13-14",
            7:"14-15",
            8:"15-16",
            9:"16-17",
            10:"17-18",
            11:"18-19",
            12:"19-20"
        }
        response = jsonify(tableSessions)
        return response 

    def get_table_prices(self):
        tablePrices = {
            1:1000,
            2:2000,
            3:3000,
            4:4000,
            5:5000,
            6:6000,
            7:7000,
            8:8000,
            9:9000,
            10:10000,
            11:11000,
            12:12000
        }
        response = jsonify(tablePrices)
        return response

    def transactionData(self):
        print("transactionData")
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)
            return jsonify("success")
        else:
            return 'Content-Type not supported!'

    def run(self, debug,  host, port):
        self.app.run(debug=debug, host=host, port=port)
        CORS(self.app, support_credentials=True)


def main():
    server = Server(__name__)
    server.run(True, host='0.0.0.0', port=5000)
    CORS(server.getApp())

if __name__ == '__main__':
    main()
    
    
