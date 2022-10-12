from flask import Flask, request, jsonify, session, render_template, flash, redirect, url_for, send_file
#  from flask_cors import CORS
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
    response = jsonify({"123": 123})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

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