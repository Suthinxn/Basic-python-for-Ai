number_rows = int(input("Enter the number of rows: "))
input_symbol = input("Enter print symbol: ")

for i in range(number_rows):
    i += 1
    print(" "*(number_rows - i)+ input_symbol*(i) + input_symbol*(i - 1) + " "*(number_rows - i))





"""
01234*43210
0123***3210
012*****210
01*******10
0*********0
***********
"""