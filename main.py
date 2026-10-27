import mysql.connector

# init all var
logged_in = False

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

# adding an input system for logging in
username = input("User: ")
password = input("password: ")

while not logged_in:
    for checkid in users:
        if users[checkid]["name"] == username:
            if users[checkid]["pin"] == password:
                print("succesfully logged in")
                logged_in = True
            else:
                print("wrong password")
    if not logged_in:
        print("Wrong combination of username and password")