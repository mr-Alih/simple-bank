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

# logging in loop
while not logged_in:
    username = input("\nUser > ").strip().lower()
    password = input("Password > ").strip()

    # Zoek de gebruiker rechtstreeks op
    user = users.get(username)

    if user is None:
        print("System > Wrong username")
        continue

    # Controleer het wachtwoord
    if str(user["pin"]) != password:
        print("System > Wrong password")
        continue

    print("System > Successfully logged in")
    logged_in = True

print("System > Welcome to your bank account!")