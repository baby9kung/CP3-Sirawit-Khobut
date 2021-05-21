print("-------------------------------")
usernameINPUT = input("USERNAME : ")
print("-------------------------------")
passwordINPUT = input("PASSWORD : ")
print("-------------------------------")
if usernameINPUT == "admin" and passwordINPUT == "123456789" :
    print("Welcome to B9K Shop")
    print("1. Pepsi : 15 THB")
    print("2. Lay   : 20 THB")
    print("3. Water : 5  THB")
    userSelected = int(input("<<"))
    if userSelected == 1 :
        amount1 = int(input("Amount : "))
        print("Price : ", amount1 * 15)
    elif userSelected == 2 :
        amount2 = int(input("Amount : "))
        print("Price : ", amount2 * 20)
    elif userSelected == 3 :
        amount3 = int(input("Amount : "))
        print("Price : ", amount3 * 5)