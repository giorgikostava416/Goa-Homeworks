while True:
    username = input("შეიყვანეთ მომხმარებლის სახელი: ")
    password = input("შეიყვანეთ პაროლი: ")
    
    if username and password:
        print("რეგისტრაცია წარმატებით დასრულდა!")
        break
    else:
        print("გთხოვთ, შეავსეთ ორივე ველი.")