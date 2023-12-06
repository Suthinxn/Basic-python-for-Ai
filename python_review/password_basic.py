"""

    ใช้ import string 
    reverse  inputที่รับมา
    ทำเป็นตัวพิมพ์เล็ก

"""
import string

# print(type(test))
def change_password(input_password):
    password = input_password.lower()
    ascii_lower = string.ascii_lowercase
    reverse_ascii_lower = ascii_lower[::-1]
    output_password = ""
    # ascii_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    
    for i in password:
        # print(i)
        # print(i in ascii_lower)
        if i in ascii_lower:
            position = reverse_ascii_lower[ascii_lower.index(i)]
            output_password += position
    return output_password
    # print(reverse_ascii_lower)
        

    # print(ascii_lower)

input_password = input("Enter 5 characters: ")
print("Encryption is",change_password(input_password))