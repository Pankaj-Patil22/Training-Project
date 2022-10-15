from Actions.transaction_service import TransactionService
from  Repositories.table_repository import TableRepository
from  Repositories.order_repository import OrderRepositry
from  Repositories.items_repository import ItemsRepository
from  Repositories.menu_repository import MenuRepository
import json
from sqlite3 import Date

class TransactionServiceImpl(TransactionService):
    def set_transaction_data(self, json_data):
        print("doing reservation")
        reservation_id = self.validate_and_store_table(json_data["table_number"], json_data["table_time_slot_id"], json_data["table_date"])
        if reservation_id == False:
            return "reservation_failed"
        print("doing orders")
        order_id = self.validate_and_store_dishes(json_data["items"],json_data["specialInstructions"])
        if order_id == False:
            return "order_failed"
        # store_transaction_details(reservation_id, order_id, json_data["table_total_price"], json_data["total_dishes_price"])
        print("returning id")
        return int(reservation_id)
    
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

    def validate_and_store_dishes(self, dishes, specialInstructions):
        print("storing order")
        order_id=OrderRepositry.insert_order_record(specialInstructions)
        print("dishes")
        for dish in dishes:
            print("dish", dish)
            if MenuRepository.get_first_menu_record(dish['itemId']) is None:
                print("Invalid item id")
                return False
            print("calling insert_items_record")
            ItemsRepository.insert_items_record(order_id, dish['itemId'], dish['quantity'])
        return order_id
        
