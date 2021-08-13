
from math import ceil


n = int(input())

def lucky_alive(n):
    pre_list = [i for i in range(1,n+1)]
    i = 0

    while n > 3:
        while i < n+3: # looping till greater than n+3 dont know why
            pre_list[i] =  ' ' # replacing list value which are to be del.
            i += 2

        n = ceil(n/2) # dividing list length by 2

        if n % 2 == 0:
            i = 1 # if prelist is even then sword at 1 person and 2nd person to be deleted
        else:
            i = 0
    return pre_list

print(lucky_alive(n))

