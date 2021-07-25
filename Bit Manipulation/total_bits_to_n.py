n = int(input('enter n value: '))

def raise_to_x(n):
    x = 0
    while (1 << x) <= n:
        x += 1
    return x - 1

def solution(s):
    total_count = 0
    for element in range(s):
        count = 0
        while element != 0:
            element &= element -1
            count += 1
        total_count += count

    return total_count

def total_bit_in_range(n):
    x = raise_to_x(n)
    msb_bits = (n - (1 << x) + 1)
    res = ((1 << x-1) * x) + msb_bits + solution(msb_bits)

    return res    

# print(total_bit_in_range(n))

def countSetBits(n):
    n += 1
    powerof2 = 2
    cnt = n //  2

    while powerof2 <= n:
        groups = n // powerof2 
        cnt += (groups//2)  * powerof2

        if (groups & 1):
            cnt += n % powerof2
        else:
            cnt += 0

        powerof2 <<= 1

    return cnt

print(countSetBits(n))