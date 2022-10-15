import json
from sqlite3 import Date
from flask import session
import Models.table_model as table_model
from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(bind=table_model.engine))

class TableRepository:
    
    @staticmethod
    def insert_time_slots(start_time, end_time):
        time_slots = table_model.TimeSlots(start_time, end_time)
        session.add(time_slots)
        session.commit()

    @staticmethod
    def insert_table_reservations(date, time_slot_id, reservations_table) -> int:
        table_reservations = table_model.TableReservations(
            date, time_slot_id, reservations_table)
        session.add(table_reservations)
        session.commit()

    @staticmethod
    def get_available_tables(slot_id, date):
        tables = session.query(table_model.TableReservations).filter(
            table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).first()
        if tables is None:
            return table_model.TableReservations(date, slot_id,[0 for i in range(12)])
        return tables
    
    @staticmethod
    def insert_reservation(table_number, table_time_slot_id, table_date) -> None:
        if (TableRepository.already_entry_made(table_time_slot_id, table_date)):
            return TableRepository.update_reservation(table_number, table_time_slot_id, table_date)

        else:
            reservation = [
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
                1 if str(table_number) == '12' else 0
            ]
            return TableRepository.insert_table_reservations(table_date, table_time_slot_id, reservation)

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
        else:
            return None

    @staticmethod
    def already_entry_made(table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        if len(tables) > 0:
            return True
        return False

    @staticmethod
    def get_tables(slot_id, date) -> list:
        tables = session.query(table_model.TableReservations).filter(
            table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).all()
        return tables

    @staticmethod
    def update_reservation(table_number, table_time_slot_id, table_date) -> int:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        for t in tables:
            print(t, "\n\n ghghgjhgjh")
            if getattr(t, TableRepository.getTableMaking(str(table_number))) == 0:
                setattr(t, TableRepository.getTableMaking(str(table_number)), "1")
                print("got table ")
                session.commit()
                print("returning id")
                return t.id
        print("No table available")
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
        else:
            return None

    @staticmethod
    def is_table_available(table, table_time_slot_id, table_date) -> bool:
        tables = TableRepository.get_tables(table_time_slot_id, table_date)
        if (tables is None or len(tables) == 0):
            return True
        for t in tables:
            print(t, "\n\n fu")
            if getattr(t, TableRepository.getTableMaking(str(table))) == 0:
                return True
        return False

# date = Date(2022, 10, 13)
# time_slot_id = 6
# one = 0
# two = 1
# three = 0
# four = 0
# five = 0
# six = 0
# seven = 0
# eight = 1
# nine = 0
# ten = 0
# eleven = 0
# twelve = 1

# arr = [one, two, three,
#        four, five, six, seven, eight, nine, ten, eleven, twelve]
# insert_table_reservations(date, time_slot_id, arr)

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

# run only once to create the database
# for i in range(8, 20,1):
#     start_time = i
#     end_time = i+1
#     print(start_time, end_time)

#     insert_time_slots(start_time, end_time)

# for i in get_time_slots():
#     print(i.start_time, i.end_time)
