""" แปลงเลขอารบิกเป็นเลขไทย
    - รับตัวเลขอารบิก 5 ตัว
    - อารบิก --> ไทย
    - ความรู้เรื่อง string

"""
import string
input_num = input("Enter only 5 Arabic number: ")
# print(input_num)
def switch_arabic_to_thai (input_num):
    # thai_number = "๐๑๒๓๔๕๖๗๘๙"
    thai_number = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"]
    arabic_number = "0123456789"
    output_num = ""

    for i in input_num:
        position_arabic = arabic_number.index(i)
        position_thai = thai_number[position_arabic]
        output_num += position_thai 

    return output_num



print("Thai number is",switch_arabic_to_thai(input_num))                      

