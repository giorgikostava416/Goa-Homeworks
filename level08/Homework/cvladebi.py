a = int(input("შეთანხმეთ a: "))
b = int(input("შეთანხმეთ b: "))
c = int(input("შეთანხმეთ c: "))

is_a_greatest = (a > b) and (a > c)
is_b_middle = (a < b < c) or (c < b < a)
is_c_least = (c < a) and (c < b)

print("is_a_greatest:", is_a_greatest)
print("is_b_middle:", is_b_middle)
print("is_c_least:", is_c_least)