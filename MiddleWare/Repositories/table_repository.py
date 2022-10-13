from turtle import update
from flask import session
import Models.table_model as table_model
from sqlalchemy.orm import sessionmaker, scoped_session

class TableRepository:
    session = scoped_session(sessionmaker(bind=table_model.engine))

    @staticmethod
    def insert_time_slots(start_time, end_time) -> None:
        time_slots = table_model.TimeSlots(start_time, end_time)    
        TableRepository.session.add(time_slots)
        TableRepository.session.commit()
        

    # *args or array of objects for the table numbers
    @staticmethod
    def insert_table_reservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve) -> int:
        table_reservations = table_model.TableReservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
        TableRepository.session.add(table_reservations)
        TableRepository.session.commit()
        return table_reservations.id

    # need to change this method name 
    @staticmethod
    def get_available_tables(slot_id, date) -> list:
        tables = TableRepository.session.query(table_model.TableReservations).filter(table_model.TableReservations.time_slot_id==slot_id, table_model.TableReservations.date==date).all()
        return tables
    
    @staticmethod
    def is_table_available(table, table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_available_tables(table_time_slot_id, table_date)
        if (tables is None or len(tables) == 0):
            return True
        for t in tables:
            print(t,"\n\n fu")
            if getattr(t, TableRepository.getTableMaking(str(table))) == 0:
                return True
        return False

    @staticmethod
    def already_entry_made(table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_available_tables(table_time_slot_id, table_date)
        if len(tables) > 0:
            return True
        return False

    @staticmethod
    def insert_reservation(table_number, table_time_slot_id, table_date) -> None:
        if (TableRepository.already_entry_made(table_time_slot_id, table_date)):
            return TableRepository.update_reservation(table_number, table_time_slot_id, table_date)
        return TableRepository.insert_table_reservations(table_date, table_time_slot_id,
                                                         1 if str(table_number) == '1' else 0,
                                                         1 if str(table_number) == '2' else 0,
                                                         1 if str(table_number) == '3' else 0,
                                                         1 if str(table_number) == '4' else 0,
                                                         1 if str(table_number) == '5' else 0,
                                                         1 if str(table_number) == '6' else 0,
                                                         1 if str(table_number) == '7' else 0,
                                                         1 if str(table_number) == '8' else 0,
                                                         1 if str(table_number) == '9' else 0,
                                                         1 if str(table_number) == '10' else 0,
                                                         1 if str(table_number) == '11' else 0,
                                                         1 if str(table_number) == '12' else 0)
    
    @staticmethod
    def update_reservation(table_number, table_time_slot_id, table_date) -> int:
        tables = TableRepository.get_available_tables(table_time_slot_id, table_date)
        for t in tables:
            print(t,"\n\n ghghgjhgjh")
            if getattr(t, TableRepository.getTableMaking(str(table_number))) == 0:
                setattr(t, TableRepository.getTableMaking(str(table_number)), "1")
                TableRepository.session.commit()
                return t.id
        return -1
    
    @staticmethod
    def getTableMaking(table_number) -> str:
        table_number = str(table_number)
        if (table_number == '1'):
            return 'one'
        if (table_number == '2'):
            return 'two'
        elif (table_number == '3'):
            return 'three'
        elif (table_number == '4'):
            return 'four'
        elif (table_number == '5'):
            return 'five'
        elif (table_number == '6'):
            return 'six'
        elif (table_number == '7'):
            return 'seven'
        elif (table_number == '8'):
            return 'eight'
        elif (table_number == '9'):
            return 'nine'
        elif (table_number == '10'):
            return 'ten'
        elif (table_number == '11'):
            return 'eleven'
        elif (table_number == '12'):
            return 'twelve'
        else :
            return None