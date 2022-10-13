from flask import session
import Models.items as items 
from sqlalchemy.orm import sessionmaker, scoped_session

class ItemsRepository:
    session = scoped_session(sessionmaker(bind=items.engine))

    def insert_items_record(order_id, item_id, quantity) -> int:
        items_record = items.Items(order_id, item_id, quantity)    
        ItemsRepository.session.add(items_record)
        ItemsRepository.session.commit()
        if items_record.id is None:
            raise Exception("items_record id is None")
        return items_record.id

    def get_all_items_for_order(order_id) -> list[object]:
        items_records = ItemsRepository.session.query(items.Items).filter_by(order_id=order_id).all()
        return items_records