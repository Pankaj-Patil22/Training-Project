from Actions.tables_service import TableService

from Repositories.table_repository import TableRepository
import DTO.available_table_dto as available_table_dto

class TableServiceImpl(TableService):
    def get_available_tables(self, time_slot_id, date):
        tables = TableRepository.get_available_tables(time_slot_id, date)
        if tables is None:
            return available_table_dto.AvailableTableDTO(date, time_slot_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).__dict__
        return available_table_dto.AvailableTableDTO(tables).__dict__

    def insert_table_reservations(self, date, time_slot_id, reservations):
        if TableRepository.get_available_tables(time_slot_id, date) is None:
            TableRepository.insert_table_reservation(date, time_slot_id, reservations)
            return "inserted"
        else:
            TableRepository.update_table_reservation(date, time_slot_id, reservations)
            return "updated"
