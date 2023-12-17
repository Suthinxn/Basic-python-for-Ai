
import string 

def loop_alphabet ():
    all_text = ""
    string_lower = string.ascii_lowercase
    while True:

        text_input = input("Enter string: ").lower()
        if text_input == "end":
            break
        for i in range(len(text_input)):
            if text_input[i] in string.ascii_lowercase: all_text += text_input[i]  
        # print(all_text)



    print("*"*30)
    print("*"+" "*5+"Alphabet Counting"+" "*6+"*")
    print("*"*30)
    for i in range(len(string_lower)):
        if string_lower[i] in all_text:
            # if all_text.index(string_lower[i]):
            print(f"{string_lower[i]} {all_text.count(string_lower[i])}")
        else:
            continue
        
    print("*"*30)







if __name__ == '__main__':

    loop_alphabet()
