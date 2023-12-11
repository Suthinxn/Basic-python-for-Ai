import string 

def  change_position(character_input):
    text_list =  string.ascii_uppercase
    new_character =""

    for i in range(0, len(character_input)):
        if character_input[i] == "Z":
            next_text = text_list[0]
            new_character += next_text
        elif character_input != "Z": 
            next_text = text_list[text_list.index(character_input[i])+1]
            new_character += next_text

    return new_character


if __name__ == '__main__' : 


    #input 
    character_input = input("Enter 3 characters: ").upper()

    #process
    change_position = change_position(character_input)

    #output
    print("Ciphertext is",change_position)
    