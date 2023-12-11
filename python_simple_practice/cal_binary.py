
def calculate_number (number_input):
    return (bin(number_input)[2:])


if __name__ == '__main__':
    #Input
    number_input = int(input("Enter number: "))

    #Process
    calculate_number = calculate_number(number_input)

    #Output
    print(f"{number_input} is {calculate_number} in base 2. ")


"""
Reference https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
"""