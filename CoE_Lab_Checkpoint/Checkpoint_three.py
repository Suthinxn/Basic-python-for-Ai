
def fibonacci(input_number):
    if (input_number == 0):
        return 0 
    elif(input_number == 1):
        return 1
    else:
        return (fibonacci(input_number - 2) + fibonacci(input_number - 1))

input_number = int(input("Input number of Fibonacci number: "))
for input_number in range(0, input_number):
    print(fibonacci(input_number), end = ' , ')
# print(end=)

"""
Reference : https://cyanogenmods.org/th/program-in-python-to-print-fibonacci-sequence/
"""