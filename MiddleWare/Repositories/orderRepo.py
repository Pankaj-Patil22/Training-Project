from flask import session
import Models.order as order 
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=order.engine)
session = Session()

def insert_order_record(special_instructions):
    order_record = order.Order(special_instructions)
    session.add(order_record)
    session.commit()
    if order_record.order_id is None:
        raise Exception("order_id is None")
    return order_record.order_id

def get_order_record (order_id):
    order_record = session.query(order.Order).filter_by(order_id=order_id).first()
    return order_record

def get_special_instruction(order_id):
    order_record = session.query(order.Order).filter_by(order_id=order_id).first()
    return order_record.special_instructions

