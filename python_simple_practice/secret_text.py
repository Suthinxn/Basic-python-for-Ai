"""
    การที่จะ Filter text ได้ เราต้องรู้ตำแหน่งของตัวอักษร และดูว่าตรงตามที่เราต้องการรึเปล่า
    ถ้ามีการ Filter text ที่ไม่มีคำนั้นใน text จะไม่ filter อะไร


"""


# def secret_text(text_input, filter_input):
#     number_text = len(text_input)
#     number_filter = len(filter_input)
#     number_filter = len(filter_input)
#     text_got_filter = ""
#     ใช้ index หา 
#     if filter_input in text_input:
#         for i in range(0, number_text):
#             if text_input[i] == filter_input[0]:
#                 if text_input[i + (number_filter-1)] == filter_input[-1]:
#                     for j in range(i,i + (number_filter-1)):
#                         text_got_filter += text_input[j]
#                         if len(text_got_filter) == number_filter :
#                             return text_got_filter    
#     else: 
#         return text_input

def filter_text(text_input,
                filter_input):
    num_filter = len(filter_input)
    if filter_input in text_input:
        first_positon = text_input.index(filter_input)
        # text_got_filter.replace(text_input[first_positon,first_positon+num_filter],"*")
        return text_input.replace(text_input[first_positon:first_positon+num_filter],"*"*num_filter)

    else:
        return text_input


if __name__ == "__main__":
    # Input
    text_input = input("Enter text: ")
    filter_input = input("Enter filter word: ")

    # Process
    filter_text = filter_text(text_input, filter_input)

    # Output
    quotes = '"'
    print(f"Text after filter is {quotes}{filter_text}{quotes}")

