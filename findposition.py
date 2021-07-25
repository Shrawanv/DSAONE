

n = int(input())

def find_position(n):
    if n < 1 or n & (n - 1):
        return -1
    i = 1
    pos = 1
    while (n & i) == 0:
        i <<= 1
        pos += 1

    return pos 

print(find_position(n))