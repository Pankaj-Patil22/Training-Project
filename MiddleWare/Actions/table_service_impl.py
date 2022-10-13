from Actions.tables_service import TableService

from  Repositories.table_repository import TableRepository 

class TableServiceImpl(TableService):
    def get_available_tables(time_slot_id, date):
        return TableRepository.get_available_tables(time_slot_id, date)
