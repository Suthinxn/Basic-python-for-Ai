import string
input_value = input("Enter value in mm, cm, and m: ")
input_unit = input("Enter convert in mm, cm, m: ")




def change_unit(input_value, input_unit):
    digits = string.digits 
    unit = ""
    value = ""

    for i in input_value:
        for j in range(10):
            
        # if input_value[i] 