
def average_number():
    list_number = []
    while True:
        number_input = int(input("Enter number: "))
        if number_input < 0:
            break
        list_number.append(number_input)

    print("Minimum number is",min(list_number))
    print("Maximum number is",max(list_number))

if __name__ == '__main__' :

    #output
    average_number()

