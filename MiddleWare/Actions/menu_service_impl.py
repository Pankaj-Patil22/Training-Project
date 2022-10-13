# from menu_service import Menu_service
from Actions.menu_service import Menu_service
import Repositories.menuRepo as menuRepo

class Menu_service_impl(Menu_service):
    def get_all_items(self):
        return menuRepo.get_all_menu_records()
    
    # def get_all_items(self):
    #     menu = MenuRepository()
    #     return menu.get_all_menu_records()