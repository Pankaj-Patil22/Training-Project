import json
from sqlite3 import Date
from flask import session
import Models.table_model as table_model
from sqlalchemy.orm import sessionmaker, scoped_session

Session = sessionmaker(bind=table_model.engine)

session = scoped_session(sessionmaker(bind=table_model.engine))

def insert_time_slots(start_time, end_time):
    time_slots = table_model.TimeSlots(start_time, end_time)    
    session.add(time_slots)
    session.commit()

def insert_table_reservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve):
    table_reservations = table_model.TableReservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
    session.add(table_reservations)
    session.commit()

def get_available_tables(slot_id, date):
    tables = session.query(table_model.TableReservations).filter(table_model.TableReservations.time_slot_id==slot_id, table_model.TableReservations.date==date).first()
    if tables is None:
        return table_model.TableReservations(date, slot_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    return tables

def get_table_reservations():
    table_reservations = session.query(table_model.TableReservations).all()
    return table_reservations

def get_time_slots():
    time_slots = session.query(table_model.TimeSlots).all()
    return time_slots


# for i in range(1,12):
#     date = Date(2019, 12, 2)
#     time_slot_id = i
#     one = 0
#     two = 0
#     three = 0
#     four = 0
#     five = 0
#     six = 0
#     seven = 0
#     eight = 0
#     nine = 0
#     ten = 0
#     eleven = 0
#     twelve = 1
#     insert_table_reservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)

# print(get_table_reservations())

#run only once to create the database
# for i in range(8, 20,1):
#     start_time = i
#     end_time = i+1
#     print(start_time, end_time)

#     insert_time_slots(start_time, end_time)

# for i in get_time_slots():
#     print(i.start_time, i.end_time)