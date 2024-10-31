while True:
    positive_number = float(input("შეიტანეთ დადებითი ციფრი (უარყოფითი ციფრის შემოტანა შეწყვეტს): "))
    if positive_number < 0:
        print("შეკითხვა დასრულდა.")
        break