number_rows = int(input("Enter the number of rows: "))

for i in range(number_rows):
    print(" "*i + "*"*(number_rows - i))
    i += 1
    