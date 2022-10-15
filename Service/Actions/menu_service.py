import abc
class Menu_service(abc.ABC):
    @abc.abstractclassmethod
    def get_all_items(self):
        pass
    
