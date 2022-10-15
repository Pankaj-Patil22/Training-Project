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


def insert_table_reservations(date, time_slot_id, reservations_table) -> int:
    table_reservations = table_model.TableReservations(
        date, time_slot_id, reservations_table)
    session.add(table_reservations)
    session.commit()


def get_available_tables(slot_id, date):
    tables = session.query(table_model.TableReservations).filter(
        table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).first()
    if tables is None:
        return table_model.TableReservations(date, slot_id,[0 for i in range(12)])
    return tables


def get_table_reservations():
    table_reservations = session.query(table_model.TableReservations).all()
    return table_reservations


def get_time_slots():
    time_slots = session.query(table_model.TimeSlots).all()
    return time_slots


def insert_reservation(table_number, table_time_slot_id, table_date) -> None:
    if (already_entry_made(table_time_slot_id, table_date)):
        return update_reservation(table_number, table_time_slot_id, table_date)

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
    return insert_table_reservations(table_date, table_time_slot_id, reservation)


def update_reservation(table_number, table_time_slot_id, table_date) -> int:
    tables = get_tables(table_time_slot_id, table_date)
    for t in tables:
        print(t, "\n\n ghghgjhgjh")
        if getattr(t, getTableMaking(str(table_number))) == 0:
            setattr(t, getTableMaking(
                str(table_number)), "1")
            session.commit()
            return t.id
    return -1


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


def already_entry_made(table_time_slot_id, table_date) -> bool:
    tables = get_tables(table_time_slot_id, table_date)
    if len(tables) > 0:
        return True
    return False


def get_tables(slot_id, date) -> list:
    tables = session.query(table_model.TableReservations).filter(
        table_model.TableReservations.time_slot_id == slot_id, table_model.TableReservations.date == date).all()
    return tables


def update_reservation(table_number, table_time_slot_id, table_date) -> int:
    tables = get_tables(table_time_slot_id, table_date)
    for t in tables:
        print(t, "\n\n ghghgjhgjh")
        if getattr(t, getTableMaking(str(table_number))) == 0:
            setattr(t, getTableMaking(str(table_number)), "1")
            session.commit()
            return t.id
    return -1


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


def is_table_available(table, table_time_slot_id, table_date) -> bool:
    tables = get_tables(table_time_slot_id, table_date)
    if (tables is None or len(tables) == 0):
        return True
    for t in tables:
        print(t, "\n\n fu")
        if getattr(t, getTableMaking(str(table))) == 0:
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
