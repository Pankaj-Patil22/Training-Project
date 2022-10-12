import abc
class Menu_service(abc.ABC):
    @abc.abstractclassmethod
    def get_all_items(self):
        pass
    
    
    
# print("This is Myclass")
# class Myclass(myinterface):
#       def display():
#         pass
# obj=Myclass()