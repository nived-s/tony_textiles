import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)
crs = con.cursor()


def create_customers():
    try:
        crs.execute("create table customers(cname varchar(25),mail varchar(25), uname varchar(25), passwd varchar(25))")
    except mysql.connector.errors.ProgrammingError:
        pass


def create_products():
    try:
        crs.execute("create table products(dcode int(4),item_name varchar(25), colour varchar(25), size char(1), price int(6))")
    except mysql.connector.errors.ProgrammingError:
        pass


def create_purchases():
    
    crs.execute("create table purchases(uname varchar(25),dcode int(4), dname varchar(25), date date)")
    


def main():
    crs.execute("use tony_textile_db;")
    create_customers()
    create_products()
    create_purchases()
    con.commit()


if __name__ == '__main__':
    main()