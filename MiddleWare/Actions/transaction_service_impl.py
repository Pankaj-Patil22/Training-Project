from Actions.transaction_service import TransactionService
from Repositories.table_repository import TableRepository
import json
from sqlite3 import Date
# {'items': [{'itemId': 1, 'quantity': 2, 'price': 10, 'name': 'Not so good Bangdo', 'totalPrice': 20},
#            {'itemId': 1, 'quantity': 2, 'price': 4200, 'name': 'chilli chicken', 'totalPrice': 8400},
#            {'itemId': 1, 'quantity': 2, 'price': 12345, 'name': 'Special Whole Egg Maker', 'totalPrice': 24690}
#            ],
#  'table_number': '["1","5","9"]',
#  'table_time_slot': '13-14',
#  'table_time_slot_id': '6',
#  'table_date': '2022-10-13',
#  'table_total_price': '15000',
#  'total_dishes_price': '33110'
#  }

class TransactionServiceImpl(TransactionService):
    def set_transaction_data(self, json_data):
        reservation_id = self.validate_and_store_table(json_data["table_number"], json_data["table_time_slot_id"], json_data["table_date"])
        # order_id = validate_and_store_dishes(json_data["items"])
        # store_transaction_details(reservation_id, order_id, json_data["table_total_price"], json_data["total_dishes_price"])
        return reservation_id
    
    def validate_and_store_table(self, table_numbers, table_time_slot_id, table_date):
        table_numbers = json.loads(table_numbers)
        arr = table_date.split("-")
        table_date=Date(int(arr[0]), int(arr[1]), int(arr[2]))
        if not self.tables_available(table_numbers, table_time_slot_id, table_date):
            print("Table not available")
            return False
        
        table_time_slot_id = int(table_time_slot_id)
        
        reservation_id = -1
        
        for table in table_numbers:
            if (len(table) == 0):
                print("Table number not provided", table, "asda")
            print("Table: ", table," whole arr", table_numbers)
            print(f"Table: {table} whole arr {table_numbers}")
            table = int(table)
            reservation_id = TableRepository.insert_reservation(table, table_time_slot_id, table_date)
        return reservation_id

    def tables_available(self, table_numbers, table_time_slot_id, table_date):
        for table in table_numbers:
            if not TableRepository.is_table_available(table, table_time_slot_id, table_date):
                return False
        return True