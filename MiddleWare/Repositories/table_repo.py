from flask import session
import Models.table_model as table_model
from sqlalchemy.orm import sessionmaker, scoped_session
# table_repository.py 

class model:
    def __init__(self,model) -> None:
        self.session = scoped_session(sessionmaker(bind=model.engine))

class TableReservations(model):
    def __init__(self) -> None:
        super.__init__()

    def insert_time_slots(self, start_time, end_time) -> None:
        time_slots = table_model.TimeSlots(start_time, end_time)    
        self.session.add(time_slots)
        self.session.commit()

    # *args or array of objects for the table numbers
    def insert_table_reservations(self, date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve) -> None:
        table_reservations = table_model.TableReservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
        self.session.add(table_reservations)
        self.session.commit()

    def get_available_tables(self, slot_id, date) -> list:
        tables = self.session.query(table_model.TableReservations).filter(table_model.TableReservations.time_slot_id==slot_id, table_model.TableReservations.date==date).all()
        return tables

    def get_table_reservations(self) -> list:
        table_reservations = self.session.query(table_model.TableReservations).all()
        return table_reservations

    def get_time_slots(self) -> list:
        time_slots = self.session.query(table_model.TimeSlots).all()
        return time_slots
    


def insert_time_slots(start_time, end_time):
    time_slots = table_model.TimeSlots(start_time, end_time)    
    session.add(time_slots)
    session.commit()

def insert_table_reservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve):
    table_reservations = table_model.TableReservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
    session.add(table_reservations)
    session.commit()

def get_available_tables(slot_id, date):
    tables = session.query(table_model.TableReservations).filter(table_model.TableReservations.time_slot_id==slot_id, table_model.TableReservations.date==date).all()
    print("sdf",tables)
    return tables

def get_table_reservations():
    table_reservations = session.query(table_model.TableReservations).all()
    return table_reservations

def get_time_slots():
    time_slots = session.query(table_model.TimeSlots).all()
    return time_slots