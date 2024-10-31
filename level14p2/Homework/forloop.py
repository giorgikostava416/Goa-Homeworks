start = int(input("განუსაზღვრეთ დიაპაზონის დასაწყისი: "))
end = int(input("განუსაზღვრეთ დიაპაზონის დასრულება: "))
for number in range(start, end + 1):
    if number % 2 == 0 and number % 3 == 0:
        print("ეს ციფრები არის 3-ისა და 2-ის ჯერადები:", number)
    else:
        print("არ არის 2-ისა და 3-ის ჯერადი:", number)