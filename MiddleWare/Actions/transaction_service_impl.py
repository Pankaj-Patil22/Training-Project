from Actions.transaction_service import TransactionService
import Repositories.table_repo as table_repo

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

# class TransactionServiceImpl(TransactionService):
#     def set_transaction_data(self, json_data):
#         reservation_id = validate_and_store_table(json_data["table_number"], json_data["table_time_slot_id"], json_data["table_date"])
#         order_id = validate_and_store_dishes(json_data["items"])
#         store_transaction_details(reservation_id, order_id, json_data["table_total_price"], json_data["total_dishes_price"])
        