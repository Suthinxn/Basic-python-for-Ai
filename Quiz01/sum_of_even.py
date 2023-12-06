input_number = input("Enter numbers: ").split()
# print(input_number)
# print(len(input_number))
# print(type(input_number))
# print(input_number[1])
# print(type(input_number[1]))
def check_number (input_number):
    sum_of_even = 0
    for i in range(len(input_number)) :
        if int(input_number[i])  %  2  ==  0 :    
            sum_of_even += int(input_number[i])
        else :
            pass


    return sum_of_even

print("Total:",check_number(input_number))