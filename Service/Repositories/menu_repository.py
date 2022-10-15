from flask import session
import Models.menu as menu
from sqlalchemy.orm import sessionmaker, scoped_session


session = scoped_session(sessionmaker(bind=menu.engine))

class MenuRepository:
    
    @staticmethod
    def insert_menu_record(name, description, eta, price, image, rating, veg, serving_size):
        menu_record = menu.Menu(name, description, eta, price, image, rating, veg, serving_size)    
        session.add(menu_record)
        session.commit()
        
    @staticmethod
    def get_all_menu_records():
        menu_records = session.query(menu.Menu).all()
        return menu_records
    
    @staticmethod
    def get_first_menu_record(item_id):
        return session.query(menu.Menu).filter(menu.Menu.item_id == item_id).first()
    
# insert_menu_record('Not So good Fish', 'king fish is for money, so we give it cheap. things are sometimes overrated', 30, 10, "https://th.bing.com/th/id/OIP.CdqlCxWYa-D_-_02gT5_BQHaF-?pid=ImgDet&rs=1", 4, False, 1)
# insert_menu_record('fried shrimp','shrimp that nobody likes but everybody pretends to like it. sometimes people are difficult to understand', 30, 300 ,'https://4.bp.blogspot.com/-W6diqeLrpH4/Uo6_oXq3DPI/AAAAAAAAFiI/aT8Grsj5VuU/s1600/IMG_3355.JPG', 4, False, 1)
# insert_menu_record('Not so good Bangdo', 'the most underrated not so good Bangdo, as the name implies its not so good', 5, 10, 'https://www.licious.in/blog/wp-content/uploads/2020/12/Mackerel-Fish-Fry.jpg', 1, False, 1)
# insert_menu_record('SquidGame Special', "watch squidGames if u haven't because that's our main ingredient", 60, 10000,'https://bigoven-res.cloudinary.com/image/upload/fried-calamari-b81193.jpg', 5, False, 1)
# insert_menu_record('chilli chicken', 'plain and simple makes everything perfect', 42, 4200,'https://static.vecteezy.com/system/resources/previews/003/024/459/non_2x/raw-chicken-slice-and-green-chili-on-a-chopping-board-on-table-photo.jpg', 5, False, 1)
# insert_menu_record('Special Whole Egg Maker', 'The most loved dish which has been voted for 10times back to back. Egg maker is our Specialty and our signature dish', 1, 12345,'https://th.bing.com/th/id/OIP.6sPM8uCpDDRZ3VIMUMVwGgHaE8?pid=ImgDet&rs=1', 5, False, 1)
# insert_menu_record('Chicken Biryani', 'Chicken Biryani is a South Asian dish with its origins of the Indian subcontinent. It is made with Indian spices, rice, and chicken, and sometimes raisins.', 30, 200, 'https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/chicken-biryani.jpg.webp', 4, False, 1)
# insert_menu_record('Chicken Tikka Masala', 'Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce. The sauce is usually creamy and orange-coloured. It is a variation of chicken tikka, a popular starter in Indian cuisine.', 30, 200, 'https://cafedelites.com/wp-content/uploads/2018/04/Best-Chicken-Tikka-Masala-IMAGE-1.jpg', 4, False, 1)
