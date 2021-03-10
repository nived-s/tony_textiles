import customerLogin
import customerSign

while True:
    print("""--- Welcome to Tony Textiles ---
    \t1) Login  
    \t2) Sign up
    """)  
    decision= int(input("choice: "))

    if decision == 1:
        customerLogin.main()
    elif decision == 2:
        customerSign.customer_sign()
    else:
        print("Invalid input.")


