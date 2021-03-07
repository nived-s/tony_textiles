import mysql.connector

from datetime import date

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

### skipped; table creation

#getting logined username

loginedUser= "user1"

    #loginedUser= customerSign.customerName

## Functions
def display_products_table():
    cmd= "SELECT * FROM products"
    crs.execute(cmd)
    print("\t\t\t----Available products---")
    print("\t", "-"*55)
    print("\t code\t name\t\tcolour\tsize\tprice")
    print("\t", "-"*55)
    for i in crs:
        print("\t",i[0],"\t", i[1],"\t\t", i[2],"\t", i[3],"\t", i[4])
        print("\t", "-"*55)
    #askingToQuit= input("\nPress any key to continue; ")

def display_customers_table():
    cmd= "SELECT cname, mail, uname FROM customers"
    crs.execute(cmd)
    print("\t\t\t----Customers Table---")
    print("\t", "-"*55)
    print("\t cname\t\tmail\t\t uname")
    print("\t", "-"*55)
    for i in crs:
        print("\t",i[0],"\t", i[1],"\t", i[2])
        print("\t", "-"*55)
    askingToQuit= input("\nPress any key to continue; ")
    del askingToQuit

def display_purchases_table():
    cmd= "SELECT * FROM purchases"
    crs.execute(cmd)
    print("\t\t----Purchases Table---")
    print("\t", "-"*55)
    print("\t cname\t dcode\t dname\t  date")
    print("\t", "-"*55)
    for i in crs:
        print("\t",i[0],"\t", i[1],"\t", i[2],"\t", i[3])
        print("\t", "-"*55)
    askingToQuit= input("\nPress any key to continue; ")
    del askingToQuit

def buy_dress():
    display_products_table()                        # display avilable items in products table

    print(" ")
    customerInput= int(input("Enter dress code: "))
    print(" ")

    
    today= date.today()
    day= today.strftime("%Y/%m/%d")
    
    # checking for dcode...showing purchase
    crs.execute(f"select * from products where dcode = '{customerInput}'")  
    for i in crs:
        print("Purchase successful.....\n")
        print("Your purchase:")
        print("\t code\t name\t\tcolour\tsize\tprice")
        print("\t", "-"*55)
        print("\t",i[0],"\t", i[1],"\t\t", i[2],"\t", i[3],"\t", i[4])
        print("\t", "-"*55)

        # inserting purchase to table purchases
        crs.execute(f"insert into purchases values('{loginedUser}', '{i[0]}', '{i[1]}', '{day}')")
        con.commit()
    
    # deleting product from table
    crs.execute(f"delete from products where dcode = '{customerInput}'")
    con.commit()   

    askingToQuit= input("\nPress any key to continue; ")
    del askingToQuit

    ## going back to main_menu
    print("\n", "*"*80)
    main_menu()
def view_purchase():
    # user name var should be imported from other file
    user= "user1"
    crs.execute(f"SELECT dcode, dname, date FROM purchases where uname = '{user}'")
    print("\tPurchase done till now by: ", loginedUser)
    print("\t\t\t----Purchases Table---")
    print("\t", "-"*45)
    print("\t dcode\titem_name\tdate")
    print("\t", "-"*45)
    for i in crs:
        print("\t",i[0],"\t", i[1],"\t      ", i[2])
        print("\t", "-"*45)
    askingToQuit= input("\nPress any key to continue; ")
    del askingToQuit

    ## going back to main_menu
    print("\n", "*"*80)
    main_menu()

def add_dress():
    while True:
        # input all data
        print(" ")
        dressCode= int(input("Enter dress code: "))      
        itemName= input("Enter item name: ")
        colour= input("Enter colour of dress: ")
        size= input("Enter size of dress: ")
        price= int(input("Enter price of dress: "))

        # entering data to db
        crs.execute(f"insert into products values('{dressCode}', '{itemName}', '{colour}', '{size}', '{price}')")
        con.commit()
        print("\nData added successfully...")
        
        # continue adding/ back to main menu
        ch= input("\nAdd more data: (y/n) ? ....  ")
        if ch.lower()=="n":
            break
        else:
            continue
    
    # back to main menu
    print("\n", "*"*80)
    main_menu()

def modify_price():
    display_products_table()                        # display avilable items in products table

    print(" ")
    dcodeInput= int(input("Enter dress code of product: "))
    print(" ")
    priceInput= int(input("\tEnter new price: "))

    # updating products
    crs.execute("update products set price='"+str(priceInput)+"' where dcode='"+str(dcodeInput)+"';")
    con.commit()
    print("\nupdation successful\n")

    ## going back to main_menu
    print("\n", "*"*80)
    main_menu()

def view_tables():
    print("view\t1) Customers table\t2) Products table\t3)Purchases table\n")
    choice= int(input("Enter choice: "))

    if choice==1:
        display_customers_table()
        ## going back to main_menu
        print("\n", "*"*80)
        main_menu()
    elif choice==2:
        display_products_table()
        ## going back to main_menu
        print("\n", "*"*80)
        main_menu()
    elif choice==3:
        display_purchases_table()
        ## going back to main_menu
        print("\n", "*"*80)
        main_menu()
    else:
        print("\nInvalid input...\n")
        view_tables()

def leave_shop():
    print("\nThankyou Have a nice day....")
    quit()

def main_menu():                                        # first control flow......(1)
    print("""
    \t  MAIN MENU ;
    CUSTOMER SERVICES;
    \t1) Buy Dress
    \t2) View Purchases
    
    ADMIN USE;
    \t3) Add dress
    \t4) Modify price
    \t5) View tables

    \t6) Quit
    """)

    ### skipped; admin authentication for 'admin use' in main menu
    #adminPasswd= "Thisisadmin123"
    while True:
        choice= int(input("Enter choice: "))

        if choice== 1:
            buy_dress()
            break
        
        elif choice == 2:
            view_purchase()
            break

        elif choice == 3:
            add_dress()
            break

        elif choice == 4:
            modify_price()
            break

        elif choice == 5:
            view_tables()
            break
        
        elif choice == 6:
            leave_shop()
            break

        else:
            print("Invalid input-------")

if __name__=="__main__":                        # initialising program
    main_menu()