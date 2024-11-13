
rows = 4
for i in range(rows):
    print(' ' * i + '*' * (rows - i))
for i in range(rows - 2, -1, -1):
    print(' ' * i + '*' * (rows - i))