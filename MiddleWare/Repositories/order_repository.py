from flask import session
import Models.order as order 
from sqlalchemy.orm import sessionmaker, scoped_session

# Session = sessionmaker(bind=order.engine)
# session = Session()

class OrderRepositry:
    session = scoped_session(sessionmaker(bind=order.engine))
    
    @staticmethod
    def insert_order_record(special_instructions) -> int:
        order_record = order.Order(special_instructions)
        OrderRepositry.session.add(order_record)
        OrderRepositry.session.commit()
        if order_record.order_id is None:
            raise Exception("order_id is None")
        return order_record.order_id

    @staticmethod
    def get_order_record (order_id) -> object:
        order_record = OrderRepositry.session.query(order.Order).filter_by(order_id=order_id).first()
        return order_record

    @staticmethod
    def get_special_instruction(order_id) -> str:
        # order_record = OrderRepositry.session.query(order.Order).filter_by(order_id=order_id).first()
        return OrderRepositry.get_order_record(order_id).special_instructions

