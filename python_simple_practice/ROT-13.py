"""
    -เลือกได้ว่า เข้ารหัส หรือ ถอดรหัส
    
"""
import string 

lower_text = string.ascii_lowercase + string.ascii_lowercase
upper_text = string.ascii_uppercase + string.ascii_uppercase

def encrypt_text(text_input):   
    num_input = len(text_input)
    result = ""
    for i in range(0, num_input):
        if text_input[i] in lower_text: 
            low_position = lower_text.index(text_input[i])
            result += lower_text[low_position + 13]

        elif text_input[i] in upper_text:     
            up_position = upper_text.index(text_input[i])
            result += upper_text[up_position + 13]
        else: result += text_input[i]

        # print(result)
    return result

def decrypt_text(text_input):
    num_input = len(text_input)
    result = ""
    for i in range(0, num_input):
        if text_input[i] in lower_text: 
            low_position = lower_text.index(text_input[i])
            result += lower_text[low_position - 13]

        elif text_input[i] in upper_text:     
            up_position = upper_text.index(text_input[i])
            result += upper_text[up_position - 13]
        else: result += text_input[i]

        # print(result)
    return result




if __name__ == '__main__' :

    #input
    select = "Select 2 options"
    option = " - 1 encrypt with ROT 13\n - 2 decrypt with ROT 13"
    print(f"{select}\n{option}\n")
    option_input = input("Choose option: ")
    text_input = input("Enter text: ")



    #process
    encrypt_text = encrypt_text(text_input)
    decrypt_text = decrypt_text(text_input)

    #output
    if option_input == "1": print(f'Ciphertext is "{encrypt_text}"')
    elif option_input == "2": print(f'Plaintext is "{decrypt_text}"')

