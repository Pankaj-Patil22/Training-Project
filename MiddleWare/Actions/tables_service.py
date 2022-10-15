import abc

class TableService(abc.ABC):
    @abc.abstractclassmethod
    def get_available_tables(self):
        pass
    
    def insert_table_reservations(self):
        pass