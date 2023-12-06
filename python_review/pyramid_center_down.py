number_rows = int(input("Enter the number of rows: "))
input_symbol = input("Enter print symbol: ")

for i in range(number_rows):
    print(" "*i + input_symbol*(number_rows - i) + input_symbol*((number_rows - i) -1 ) + " "*i)
    i += 1 
