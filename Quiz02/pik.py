


def check_green(input_rgb):
    
    r = int(input_rgb[0])
    g = int(input_rgb[1])
    b = int(input_rgb[2])
    avg_rb = (r+b) / 2

    for i in range(0, len(input_rgb)):
        check = int(input_rgb[i]) >= 0 and int(input_rgb[i]) <= 255
        if  check == False:
            return "Value Out of Range"
    if (g - avg_rb) >= 30:
        return "Green"
    else:
        return "Not Green"




if __name__  == '__main__':

    #input
    input_rgb = input("RGB: ").split(',')

    #output
    print(check_green(input_rgb))
    # print(input_rgb)
