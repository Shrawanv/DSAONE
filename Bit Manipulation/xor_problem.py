# problem statement
# find the only non repeating element in an array where every element repeats twice.

# arr = [2,4,7,9,2,4]
# arr  = list(map(int,input("Enter array values: ").strip().split(" ")))

def two_distinct(arr):
    xor = 0
    res1 = 0
    res2 = 0
    for element in arr:
        xor ^= element
    
    set_bit = xor & ~(xor - 1)

    for element in arr:
        if element & set_bit == 0:
            res2 ^= element
        else:
            res1 ^= element
    return res1, res2

# ///////////
# import sys

# print(8*sys.getsizeof(int))