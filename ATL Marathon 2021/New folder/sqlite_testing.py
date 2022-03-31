import sqlite3

connection = sqlite3.connect('vital_signs.db')
cursor = connection.cursor()
"""cursor.execute('''CREATE TABLE IF NOT EXISTS readings
              (id int PRIMARY KEY,
              bp INT,
              pulse INT,
              temp INT,
              breath INT,
              time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

connection.commit()
""" 

# Inserting
"""
value = [(2, 120, 70, 35, 100)]
cursor.executemany("INSERT INTO readings (id, bp, pulse, temp, breath) VALUES (?, ?, ?, ?, ?)", value)
"""

# cursor.execute('''CREATE TABLE IF NOT EXIS''')


cursor.execute('SELECT * FROM readings')
result = cursor.fetchall()
for i in result:
  print(i)
connection.close()