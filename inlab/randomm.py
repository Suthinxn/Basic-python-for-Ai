import random

rand_num = random.randint(0, 20)
guess_num = int(input("Enter guessing number (0-20) : "))

diff = abs(rand_num - guess_num)
print('Random number is {}, your guessing number is {}.'.format(
    rand_num,
    guess_num))

if guess_num >= 0 and guess_num <= 20: 
    if rand_num == guess_num :
        print("Good job, it\' equal.")
    elif diff 
                                                        