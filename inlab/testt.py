import datetime

def first_n(n):

    num, nums = 0, []
    while num < n:
        nums.append(num)
        num  += 1

    return nums

start_time = datetime.datetime.now()
sum_of_first_n = sum(first_n(1_000.)
stop_time = datetime.datetime.now()

print('time = ',(stop_time - start_time))