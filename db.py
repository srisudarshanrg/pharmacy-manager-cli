import mysql.connector
from credentials import password

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    port=5000
)

cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS pharmacy_db")
cur.execute("USE pharmacy_db")
