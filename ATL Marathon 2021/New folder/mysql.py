"""import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Password123#",
  database="test"
)

cursor = db.cursor()
"""

"""
CREATE TABLE patients_readings (
  id int PRIMARY KEY,
  name CHAR(20),
  timestamp TIMESTAMP,
  bp INT,
  pulse INT,
  temp INT,
  breath INT
);

CREATE TABLE patients_values (

);

INSERT INTO patients_readings (id, name, timestamp, bp, pulse, temp, breath);
"""


import mysql.connector

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE TABLE")

# Inserting values
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

# Getting data 
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
"""