

def target_snake(path_input):
    position_x = 0
    position_y = 0
    found_snake = []
    return_found_snake = ""

    for i in range(0,len(path_input)):

        if path_input[i] == "^":
            position_y += 1
            # print(position_y)
        elif path_input[i] == ">":
            position_x += 1
            # print(position_x)
        elif path_input[i] == "<":
            position_x -= 1
            # print(position_x)
        elif path_input[i] == "v":
            position_y -= 1
            # print(position_y)
        elif path_input[i] == "x":
            found_snake.append((position_x,position_y))
    
    for i in range(0,len(found_snake)):
        return_found_snake += " "+str(found_snake[i])
            # return_found_snake += str(found_snake[i])


    return return_found_snake





if __name__  ==  '__main__' :

    path_input = input("Path: ")

    target_snake = target_snake(path_input)

    if  "x" not in path_input:
        print("Not Found")
    else:    
        print(f"Locations:{target_snake}")