import mysql.connector
import tony_textiles
import tables

# establishing database connectivity
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)
crs = con.cursor()

# open/create db
try:
    crs.execute('USE tony_textile_db;')

except mysql.connector.errors.ProgrammingError:
    crs.execute('CREATE DATABASE tony_textile_db;')
    crs.execute('USE tony_textile_db;')
    tables.main()
    con.commit()

# inputing values

def user_authentication(customerUsernameInput, customerPasswordInput):
    crs.execute("SELECT uname FROM customers;")
    rows = crs.fetchall()
    availableUsernameList = []

    # check for username
    for eachName in rows:
        availableUsernameList.append(str(eachName[0]))
    
    if customerUsernameInput in availableUsernameList:

        # check for password
        crs.execute("SELECT passwd FROM customers where uname='" +
                    str(customerUsernameInput)+"';")
        originalPassword = crs.fetchone()

        if customerPasswordInput == originalPassword[0]:
            print(">>> login success ")
            tony_textiles.main_menu()
        else:
            print("Incorrect Password.\n")
            user_input()

    else:
        print("No username found.\n")
        user_input()

# making login
def user_input():
    inputUsername = input("\nEnter username:")
    inputPassword = input("Enter password:")
    user_authentication(inputUsername, inputPassword)


def main():
    user_input()
