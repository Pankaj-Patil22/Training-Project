from datetime import datetime
from decimal import FloatOperation
from email.policy import default
from click import echo
from sqlalchemy import DATE, TIMESTAMP, VARCHAR, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.sql import func

engine = create_engine('sqlite:///sqlalchemy.sqlite',echo=True)

base = declarative_base()

class Menu (base):
    __tablename__ = 'menu'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100), nullable=False)
    description = Column(VARCHAR(500), nullable=False)
    eta = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    image = Column(VARCHAR(200), nullable=False)
    rating = Column(Integer, nullable=False)
    veg = Column(Boolean, nullable=False)
    serving_size = Column(Integer, nullable=False)
    
    
    def __init__(self, name, description, eta, price, image, rating, veg, serving_size):
        self.name = name
        self.description = description
        self.eta = eta
        self.price = price
        self.image = image
        self.rating = rating
        self.veg = veg
        self.serving_size = serving_size
        
base.metadata.create_all(engine)