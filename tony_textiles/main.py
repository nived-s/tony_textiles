from subprocess import Popen
import customerLogin
import customerSign

while True:
    print("""Welcome to Tony Textiles :)
    \t1) Login  
    \t2) Sign up""")  
    decision= int(input("choice: "))

    if decision==1:
        Popen("python customerLogin.py")
        break
    elif decision==2:
        customerSign.customer_sign()       
        break
    else:
        print("Invalid input...")


