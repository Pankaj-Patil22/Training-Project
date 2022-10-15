
from sqlalchemy import VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)

base = declarative_base()


class Items (base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    item_id = Column(Integer)
    quantity = Column(Integer, nullable=False)

    def __init__(self, order_id, item_id, quantity):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity


base.metadata.create_all(engine)
