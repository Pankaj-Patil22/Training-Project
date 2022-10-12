import sqlite3

connection = sqlite3.connect('CAFEDB.db')

with open('reservations_table.sql') as f:
    connection.executescript(f.read())

with open('time_slot.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO time_slot VALUES (1, '8', '9')")
cursor.execute("INSERT INTO time_slot VALUES (2, '9', '10')")
cursor.execute("INSERT INTO time_slot VALUES (3, '10', '11')")
cursor.execute("INSERT INTO time_slot VALUES (4, '11', '12')")
cursor.execute("INSERT INTO time_slot VALUES (5, '12', '13')")
cursor.execute("INSERT INTO time_slot VALUES (6, '13', '14')")
cursor.execute("INSERT INTO time_slot VALUES (7, '14', '15')")
cursor.execute("INSERT INTO time_slot VALUES (8, '15', '16')")
cursor.execute("INSERT INTO time_slot VALUES (9, '16', '17')")
cursor.execute("INSERT INTO time_slot VALUES (10, '17', '18')")
cursor.execute("INSERT INTO time_slot VALUES (11, '18', '19')")
cursor.execute("INSERT INTO time_slot VALUES (12, '19', '20')")

cursor = connection.cursor()

connection.commit()
connection.close()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

# engine = create_engine('sqlite:///C:\\path\\to\\foo.db')

# class TableFeatues:
#     def __init__(self, table_name, table_id, table_type, table_size, table_miss_config):
#         self.table_name = table_name
#         self.table_id = table_id
#         self.table_type = table_type
#         self.table_size = table_size
#         self.table_miss_config = table_miss_configx
