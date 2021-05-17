username = input("username: ")
passwords = input("password :")
if username == "admin" and passwords == "12345":
    print ("done!!!")
else :
    print("wrong passwords")
    if username == "admin" and passwords == "1234":
        print("Done !")
        print("----- iShop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")
        userSelected = int(input(">>"))
        if userSelected == 1:
            price = int(input("Price (THB): "))
            vat = 7
            result = price + (price * 7 / 100)
            print (result)
        elif userSelected == 2:
           price1 = int(input("First Product Price : "))
           price2 = int(input("Second Product Price : "))
           print(price1+price2)
