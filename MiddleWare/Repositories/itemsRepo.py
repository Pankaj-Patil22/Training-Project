from flask import session
import Models.items as items 
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=items.engine)
session = Session()

def insert_items_record(order_id, item_id, quantity):
    items_record = items.Items(order_id, item_id, quantity)    
    session.add(items_record)
    session.commit()

def get_all_items_for_order(order_id):
    items_records = session.query(items.Items).filter_by(order_id=order_id).all()
    return items_records