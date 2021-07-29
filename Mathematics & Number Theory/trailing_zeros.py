
n = int(input())

def trailing_zeros(n):
    i = 5
    res = 0
    while i <= n:
        res += n // i
        i *= 5

    return res

print(f'Trailing zeros in factorial of {n} is {trailing_zeros(n)}')