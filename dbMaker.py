import sqlite3 as sq3


conn = sq3.connect('Shop.sqlite')
cursor = conn.cursor()

# cursor.execute("PRAGMA foreign_keys = ON;")
# cursor.execute('''
#     DROP TABLE Storage
#     ''')
# conn.commit()
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Customer(
#         id INTEGER PRIMARY KEY NOT NULL,
#         name VARCHAR(50),
#         surname VARCHAR(50),
#         phone_number VARCHAR(10),
#         create_time VARCHAR(50)
#         )
#     ''')
# conn.commit()
# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Invoice(
#         id INTEGER PRIMARY KEY NOT NULL,
#         name VARCHAR(50),
#         price INTEGER,
#         user_id INTEGER NOT NULL,
#         FOREIGN KEY(user_id)
#             REFERENCES Customer (id)
#         )
#     ''')
# conn.commit()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Invoice (
#         id INTEGER PRIMARY KEY NOT NULL,
#         name VARCHAR(50),
#         price INTEGER,
#         user_id INTEGER,
#         create_time VARCHAR(50)
#     )
# ''')
# conn.commit()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Storage(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        count INTEGER,
        create_time VARCHAR(50)
        )
    ''')
conn.commit()
# id = 0
# cursor = conn.cursor()
# query = cursor.execute('''
#     SELECT * FROM Customer WHERE id=?
# ''',(id,))
# result = query.fetchall()
# print(result)
# conn.commit()
