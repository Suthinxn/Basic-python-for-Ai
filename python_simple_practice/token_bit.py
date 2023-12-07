"""
Token 
- จำนวนอักขระใน Token % ผลบวกของเลข1 ในToken = 0 ถูกสลาก

"""

token = input("Enter Token number: ")
# print(token)
number_token = len(token)
# print(type(number_token))
# print(number_token)

number_zero = token.count('0')
# print(type(number_zero))
# print("number_zero", number_zero)
number_one = token.count('1')
# print("number_one", number_one)

token_mod = number_token % number_one

if number_token == (number_zero + number_one):
    if token_mod == number_zero:
        print("You get jackpot!!")
    else:
        print("See you next time, have a nice day.")
else:
    print("Your token is invalid")










# import string

# token_str= input("Enter Token number: ")
# token_len = len(token_str)

# number_zero = token_str.count('0')
# number_one = token_str.count('1')

# sum_of_one =int(number_one)
# token_mod = int(len(token_len)) % sum_of_one


# if token_len == (number_zero + number_one):
#     if token_mod == number_zero:
#         print("Your get jackpot!!")
#     else:
#         print("See you next time, have a nice day.")
# else:
#     print("Your token is invalid")
# number_zero =  token_str.count('0')
# number_one = token_str.count('1')
# sum_of_one = 1 * int(number_one)
# mody = token_len % (sum_of_one)
# # print(token_len)
# # print(number_zero, "and", number_one)
# # print("t",token_len)
# # print("s",(number_zero + number_one))
# if token_len == (number_zero + number_one):
#     if int(mody) == int(number_zero):
#         print("You get jackpot!!")
#     elif sum_of_one != number_zero:
#         print("See you next time, have a nice day.")
# else:
#     print("Your token is invalid")