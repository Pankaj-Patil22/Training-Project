from Actions.tables_service import TableService

import Repositories.table_repo as table_repo

class TableServiceImpl(TableService):
    def get_available_tables(time_slot_id, date):
        tables = table_repo.get_available_tables(time_slot_id, date)
        return tables