''' Q. Given an array, every element in array appears thrice except one which occurs once.
#    Find that element which does not appear thrice.

    #  A = [1,2,4,3,3,2,2,3,1,1]
    #  output = 4
    # A = [0,0,0,1]
    #  output = 1
'''

#  1) Hash Map + Linear Traversal

arr = [1,2,4,3,3,2,2,3,1,1]
# arr = [0,0,0,1]

# def distinct_number(arr):
#     mydict = {}
    
#     for element in arr:
#         if element in mydict:
#             mydict[element] += 1
#         else:
#             mydict[element] = 1
        
#     for element in mydict:
#         if mydict[element] == 1:
#             return element

# print(distinct_number(arr))

''' 2) Sorting and Linear Traversal
  time complexity of O(NlogN + N)
  log N <= 32 '''

def distinct_number(arr):
    arr = sorted(arr)
    if arr[0] != arr[1]: # border case 1
        return arr[0]
    elif arr[-1] != arr[-2]: # border case 2
        return arr[-1]
    else:
        pos = 1
        while pos <= len(arr):
            if arr[pos] != arr[pos-1]:
                return arr[pos]
            else:
                pos += 3

''' Bit Manipulation Method '''

def unique_element(arr):
    once = 0
    twice = 0

    for element in arr:
        once = (once ^ element) & ~(twice)
        twice = (twice ^ element) & ~(once)

    return once

print(distinct_number(arr))
print(unique_element(arr))