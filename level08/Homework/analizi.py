score = int(input("შეთანხმეთ ქულა (0-100): "))

is_pass = score >= 50
is_high_pass = 75 < score < 90
is_perfect = score == 100
is_failing = score < 50

print("is_pass:", is_pass)
print("is_high_pass:", is_high_pass)
print("is_perfect:", is_perfect)
print("is_failing:", is_failing)