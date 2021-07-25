x, y, l, r = list(map(int, input().split()))

def copy_bits(x, y, l, r):
    mask = None
    for i in range(l, r+1):
        mask = 1 << (i-1)

        if y & mask:
            x = x | mask
    return x
        

print(copy_bits(x, y, l, r))
# print(bin(11))
# print(bin(6))