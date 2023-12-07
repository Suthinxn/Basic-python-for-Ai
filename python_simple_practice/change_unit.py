
def change_unit(input_value, input_unit):

    if "mm" in input_value :
        result = float(input_value.strip("mm"))

        if  input_unit == "mm":
            return str(result) + input_unit
        elif input_unit == "cm":
            return str(result/10) + input_unit
        elif input_unit == "m":
            return str(result/1000) + input_unit


    elif "cm" in input_value :
        result = float(input_value.strip("cm"))
        
        if input_unit == "mm":
            return str(result*10) + input_unit
        elif input_unit == "cm":
            return str(result) + input_unit
        elif input_unit == "m":
            return str(result/100) + input_unit


    elif "m" in input_value :
        result = float(input_value.strip("m"))

        if input_unit == "mm":
            return str(result*1000) + input_unit
        elif input_unit == "cm":
            return str(result*100) + input_unit    
        elif input_unit == "m":
            return str(result) + input_unit


input_value = input("Enter value in mm, cm, and m: ")
input_unit = input("Enter unit to convert in mm, cm, m: ")

print("Value after unit conversion is",change_unit(input_value, input_unit))
