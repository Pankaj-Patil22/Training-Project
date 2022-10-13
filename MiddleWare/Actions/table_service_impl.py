from Actions.tables_service import TableService

import Repositories.table_repo as table_repo
import DTO.available_table_dto as available_table_dto

class TableServiceImpl(TableService):
    def get_available_tables(time_slot_id, date):
        tables = table_repo.get_available_tables(time_slot_id, date)
        if tables is None:
            return available_table_dto.AvailableTableDTO(date, time_slot_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).__dict__
        return available_table_dto.AvailableTableDTO(tables).__dict__

    def insert_table_reservations(date, time_slot_id, reservations):
        
        table_repo.insert_table_reservations(date, time_slot_id, reservations)