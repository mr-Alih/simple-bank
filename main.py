import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="bank_system",
)

cursor = conn.cursor(dictionary=True)   # rows come back as dicts
cursor.execute("SELECT * FROM users")

# the whole table as a dictionary keyed by first name
users = {row["name"].split()[0].lower(): row for row in cursor.fetchall()}

cursor.close()
conn.close()