from sqlalchemy import DATE, TIMESTAMP, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql import func

engine = create_engine('sqlite:///sqlalchemy.sqlite',echo=True)

base = declarative_base()

class TimeSlots (base):
    __tablename__ = 'time_slots'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(VARCHAR(2))
    end_time = Column(VARCHAR(2))


    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

class TableReservations (base):
    __tablename__ = 'table_reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created=Column(TIMESTAMP, server_default=func.now(), nullable=False)
    date=Column(DATE, nullable=False)
    time_slot_id = Column(Integer, ForeignKey('time_slots.id'))
    one=Column(Integer, default = 0)
    two=Column(Integer, default = 0)
    three=Column(Integer, default = 0)
    four=Column(Integer, default = 0)
    five=Column(Integer, default = 0)
    six=Column(Integer, default = 0)
    seven=Column(Integer, default = 0)
    eight=Column(Integer, default = 0)
    nine=Column(Integer, default = 0)
    ten=Column(Integer, default = 0)
    eleven=Column(Integer, default = 0)
    twelve=Column(Integer, default = 0)

    def __init__(self, date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve):
        self.date = date
        self.time_slot_id = time_slot_id
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.eleven = eleven
        self.twelve = twelve

# class TablePrices (base):
#     __tablename__ = 'table_prices'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     one=Column(Integer, default = 0)
#     two=Column(Integer, default = 0)
#     three=Column(Integer, default = 0)
#     four=Column(Integer, default = 0)
#     five=Column(Integer, default = 0)
#     six=Column(Integer, default = 0)
#     seven=Column(Integer, default = 0)
#     eight=Column(Integer, default = 0)
#     nine=Column(Integer, default = 0)
#     ten=Column(Integer, default = 0)
#     eleven=Column(Integer, default = 0)
#     twelve=Column(Integer, default = 0)

#     def __init__(self, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve):
#         self.one = one
#         self.two = two
#         self.three = three
#         self.four = four
#         self.five = five
#         self.six = six
#         self.seven = seven
#         self.eight = eight
#         self.nine = nine
#         self.ten = ten
#         self.eleven = eleven
#         self.twelve = twelve

base.metadata.create_all(engine)