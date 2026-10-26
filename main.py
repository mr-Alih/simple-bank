import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="bank_system",
)
# connection start

cursor = conn.cursor(dictionary=True)   # rows come back as dicts
cursor.execute("SELECT * FROM users")
# what branch/actual scheme

# the whole table as a dictionary keyed by first name
users = {row["name"].split()[0].lower(): row for row in cursor.fetchall()}

cursor.close()
conn.close()

# real code here. 
print()