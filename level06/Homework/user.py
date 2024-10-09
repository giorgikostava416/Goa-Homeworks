first_name = input("შეიყვანეთ თქვენი სახელი: ")
last_name = input("შეიყვანეთ თქვენი გვარი: ")
mother_first_name = input("შეიყვანეთ დედის სახელი: ")
mother_last_name = input("შეიყვანეთ დედის გვარი: ")
favorite_color = input("შეიყვანეთ საყვარელი ფერი: ")
favorite_car = input("შეიყვანეთ საყვარელი მანქანა: ")


hobbies = [
    input("შეიყვანეთ საყვარელი ჰობი №1: "),
    input("შეიყვანეთ საყვარელი ჰობი №2: "),
    input("შეიყვანეთ საყვარელი ჰობი №3: ")
]


statement = (f"მომხმარებლის სახელი არის {first_name} {last_name}, "
             f"მისი დედის სახელი {mother_first_name} {mother_last_name}, "
             f"საყვარელი ფერი არის {favorite_color}, "
             f"საყვარელი მანქანა არის {favorite_car}, "
             f"მიუხედავად ამისა, მისი საყვარელი ჰობებია: {', '.join(hobbies)}.")


print(statement)