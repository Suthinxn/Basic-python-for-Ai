input_number = input("Input: ").split(',')
n = int(input_number)
# print(input_number)

def check_number (n):
    count = 0
    for i in len(input_number):
        if len(input_number) == int(input_number[i]):
            count += 1
        i += 1
    return count

print("Output",check_number(n))