import mysql.connector

# init all var
logged_in = False
hold_user = False

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
users = {
    row["username"].split()[0].lower(): row
    for row in cursor.fetchall()
}

cursor.close()
conn.close()

# add or subtract money
def substitute(amount, userid):
    cursor.execute(
        "UPDATE users SET balance = balance + %s WHERE id = %s",
        (amount, user[userid])
    )

    conn.commit()

# real code here. 
def static():
    print("\nUsername: ", user["name"], user["username"])
    print("Balance: ", user["balance"])
    print("Nr ", user["id"], "St", user["bank_number"])

def transfer():
    choice = input("Transfer Username > ")
    CUN = user[str(choice)]
    if CUN == None:
        print("System > Error 404 not found")
        transfer()
    print("Found user. ", CUN)
    choice = input("Amount to transfer > ")
    substitute(choice, CUN)


# after logging in menu
def menu():
    print("\n1: Transfer")
    print("2: Actuate")
    print("3: History")
    choice = int(input("What do you want to do > "))
    if choice == 1:
        transfer()
    # elif menu == 2:
    #     # actuate()
    # elif menu == 3:
    else:
        print("System > Error 404 not found")
        menu()

# logging in loop
while not logged_in:
    if hold_user == False:
        username = input("\nUser > ").strip().lower()
    password = input("Password > ").strip()
    if password == "exit":
        hold_user = False
        continue

    # Zoek de gebruiker rechtstreeks op
    user = users.get(username)

    if user is None:
        print("System > Wrong username")
        continue

    # Controleer het wachtwoord
    if str(user["pin"]) != password:
        # keep hold of the username.
        print("System > Wrong password")
        hold_user = True
        continue

    print("System > Successfully logged in")
    logged_in = True
    hold_user = False

print("\nSystem > Welcome to your bank account!")
static()
menu()