number = int(input("შეიყვანეთ ორნიშნა რიცხვი: "))
if 10 <= number <= 99:
    digit1 = number // 10 
    digit2 = number % 10
    digit_sum = digit1 + digit2
    print(f"ციფრების ჯამი არის: {digit_sum}")
else:
    print("შეიყვანეთ ორნიშნა რიცხვი!")