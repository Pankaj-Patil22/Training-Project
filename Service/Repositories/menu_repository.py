from flask import session
import Models.menu as menu
from sqlalchemy.orm import sessionmaker, scoped_session


session = scoped_session(sessionmaker(bind=menu.engine))

class MenuRepository:
    
    @staticmethod
    def insert_menu_record(name, description, eta, price, image, rating, veg, serving_size):
        menu_record = menu.Menu(name, description, eta, price, image, rating, veg, serving_size)    
        session.add(menu_record)
        session.commit()
        
    @staticmethod
    def get_all_menu_records():
        menu_records = session.query(menu.Menu).all()
        return menu_records
    
    @staticmethod
    def get_first_menu_record(item_id):
        return session.query(menu.Menu).filter(menu.Menu.item_id == item_id).first()
