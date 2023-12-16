
def average_even_number():
    counter = 1
    list_number =[]
    while counter < 21 :
        number_input = int(input(f"Enter number #{counter}: "))
        if number_input not in list_number:
            list_number.append(number_input)
        counter += 1

    list_number.sort()
    set_number = " ".join(map(str, list_number))
    # print(list_number)
    print(f"Unique numbers is {set_number}")
    number_even_position = 0
    number_len_even = 0
    for i in range(0, len(list_number), +2 ): 
        number_even_position += int(list_number[i]) 
        number_len_even += 1
    # print(number_even_position)
    avg_position_even =  float(number_even_position / number_len_even)
    print(f"Average number of even position in list is {avg_position_even:.2f}")

if __name__ == '__main__':
    average_even_number()
    
    # average_even = set( int(i) for i in range(0, input(f"Enter number #{i}: ")) if i % 2 == 0 and > -1 )

    # print(f'Unique numbers is {average_even}')
    # avg_even = sum(average_even) // len(average_even)
    # print(f"Average number of even position in list is {avg_even}")
    # i = [input("Enterr#{}".format(n+1)) for n in range(20)]
    # [number  ]