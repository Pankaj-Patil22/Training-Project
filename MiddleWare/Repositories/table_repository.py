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
    def insert_table_reservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve) -> None:
        table_reservations = table_model.TableReservations(date, time_slot_id, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)
        TableRepository.session.add(table_reservations)
        TableRepository.session.commit()

    @staticmethod
    def get_available_tables(slot_id, date) -> list:
        tables = TableRepository.session.query(table_model.TableReservations).filter(table_model.TableReservations.time_slot_id==slot_id, table_model.TableReservations.date==date).all()
        return tables