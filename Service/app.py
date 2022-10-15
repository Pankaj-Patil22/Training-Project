from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from Actions.menu_service_impl import Menu_service_impl as Menu_service
from sqlite3 import Date
import DTO.available_table_dto as available_table_dto
from Actions.table_service_impl import TableServiceImpl as TableService
from Actions.transaction_service_impl import TransactionServiceImpl as TransactionService

class FlaskAppWrapper():
    def __init__(self):
        self.app = Flask(__name__)
        self._config()
        self._add_services()
        

        @self.app.route('/getTableSessions/', methods = ['GET'])
        def __table_Sessions():
            return self.get_table_sessions()

        @self.app.route('/tables/price', methods=['GET'])
        def __table_Price():
            return self.get_table_prices()

        @self.app.route('/transactionData/', methods=['POST'])
        def __transaction_data():
            return self.transaction_data()

        @self.app.route('/tables/<int:year>/<int:month>/<int:day>/<int:time_slot_id>', methods=['GET'])
        def __available_tables(year, month, day, time_slot_id):
            return self.get_available_tables(year, month, day, time_slot_id)
        
        @self.app.route('/getMenu/', methods = ['GET'])
        def __menu():
            return self.get_Menu()
         
    def _config(self):
        CORS(self.app)
        self.app.secret_key = os.urandom(24)
    
    def _add_services(self):
        self.table_service = TableService()
        self.menu_service = Menu_service()
        self.transaction_service = TransactionService()
        
    def get_Menu(self):
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
        
    def get_available_tables(self, year, month, day, time_slot_id):
        if request.method == 'GET':
            date = Date(year, month, day)
            table_reservation = self.table_service.get_available_tables(time_slot_id, date)
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
        price = [1000, 500, 500, 1000, 1000, 500, 500, 1000, 1000, 500, 500, 1000]
        response = jsonify({"prices": price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def transaction_data(self):
        print("transactionData")
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            try:
                msg = self.transaction_service.set_transaction_data(json)
                print(msg)
                print("\n\n\n hitting success  \n\n\n")
                if (type(msg) == int):
                    return jsonify({"success": True})
            except:
                print("\n\n\n  error \n\n\n")
        print("\n\n\n hitting faild  \n\n\n")
        return jsonify({"success": False})

    def _corsify_actual_response(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    def run(self, debug,  host, port):
        self.app.run(debug=debug, host=host, port=port)


def main():
    app = FlaskAppWrapper()
    app.run(True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
    
    
# def _build_cors_preflight_response(response):
    # response.headers.add("Access-Control-Allow-Origin", "*")
    # response.headers.add("Access-Control-Allow-Headers", "*")
    # response.headers.add("Access-Control-Allow-Methods", "*")
    # return response