"""
    Comprehension
"""

# input_number = input("Enter 10 numbers: ").split()
# # print(input_number)
# result_even = {i for i in range(0,10) if int(input_number[i]) % 2 == 0 }

# print(result_even)

# print(input_number)
# result_even = {i for i in range(len(input_number)) if int(input_number[i]) % 2 == 0}
# print("Result is", result_even)
# print(type(input_number))


# input_number = input("Enter 10 numbers: ").split()
# result_even = set()
# for i in range(len(input_number)):
#     if int(input_number[i]) % 2 == 0 :
#         result_even.add(int(input_number[i]))
# print("Result is",result_even)

# 11 22 33 44 55 66 77 88 99 36
# {66, 36, 44, 22, 88}

# input_number = input("Enter 10 numbers: ").split()

result_even = set( int(i) for i in input("Enter 10 numbers: ").split() if int(i) % 2 == 0) 
print("Result is",result_even)
# result_even = set( input_number[i] for i in range (len(input_number)) if int(input_number[i]) % 2 == 0)