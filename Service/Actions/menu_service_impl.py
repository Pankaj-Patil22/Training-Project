# from menu_service import Menu_service
from Actions.menu_service import Menu_service
from Repositories.menu_repository import MenuRepository
 
class Menu_service_impl(Menu_service):
    def get_all_items(self):
        return MenuRepository.get_all_menu_records()