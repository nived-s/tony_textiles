import mysql.connector
from subprocess import Popen
import tony_textiles
import re

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
    con.commit()

# this var is exported to tony_textiles.py
customerName=" "

def customer_sign():
    name= input("Enter Your name: ")
    customerName= name
    mail= input("Mail address: ")
    username= input("Enter user name(this should be unique): ")
    password= input("Select a strong password: ")
    print(" ")
    crs.execute("SELECT uname FROM customers;")
    rows= crs.fetchall()
    availableUsernameList= []
    
    for eachName in rows:
        availableUsernameList.append(str(eachName[0]))
    
    
    '''
    How a new user is added:
        1) check if username already exists
        2) check if passwd is a common passwords in the file "commonpassword.txt"
        3) check for password stength using rejex method 

    if True; user is signed in ;)

    '''
    flag= False
    if username in availableUsernameList:
        print("Username already exists....\nTry another username\n")
        customer_sign()
    else:
        
        # common pass check
        with open("commonpasswords.txt", 'r') as f:
            data= f.read()
            dataList= data.split()
            #print(dataList)

            if password in dataList:
                print("Password enterd is a commonly occuring, try a strong password")
                #customer_sign()

        # Rejex check
        # there is some error in the rejex check method
        def uppercase_check(password):
            if re.search(' [A-Z] ', password):
                return True
            return False
        def lowercase_check(password):
            if re.search(' [a-z] ', password):
                return True
            return False
        def digit_check(password):
            if re.search(' [0-9] ', password):
                return True
            return False

        def rejex_check():
            global flag
            if len(password) >= 4 and uppercase_check(password) and lowercase_check(password) and digit_check(password):
                flag=True
                print("strong pass")
            else:
                print("Weak password\n")

        rejex_check()

        if flag:
            # inserting purchase to table customers
            crs.execute(f"insert into customers values('{customerName}', '{mail}', '{username}', '{password}')")
            con.commit()
            print(">>> signup success ")
            #Popen("python tony_textiles.py")
            tony_textiles.main_menu()
            
        else:
            print("Signing failed....")
            customer_sign()


if __name__=="__main__":                       
    customer_sign()
