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

# this var is exported to tony_textiles.py
customerName=" "

def customer_sign():
    name = input("Enter Your name: ")
    customerName = name
    mail = input("Mail address: ")
    username = input("Enter user name(this should be unique): ")
    password = input("Select a strong password: ")
    print(" ")
    crs.execute("SELECT uname FROM customers;")
    rows = crs.fetchall()
    availableUsernameList = []
    
    for eachName in rows:
        availableUsernameList.append(str(eachName[0]))
    
    if username in availableUsernameList:
        print("Username already exists....\nTry another username\n")
        customer_sign()

    elif username not in availableUsernameList:
        # inserting purchase to table customers
        crs.execute(f"insert into customers values('{customerName}', '{mail}', '{username}', '{password}')")
        con.commit()
        print(">>> signup success ")
        #Popen("python tony_textiles.py")
        tony_textiles.main_menu()
            
    else:
        print("Signing failed! Try again.")
        customer_sign()


if __name__=="__main__":                       
    customer_sign()
