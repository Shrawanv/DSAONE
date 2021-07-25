n = int(input())

def ispowerof2(n):

    if n & (n - 1):
        return False
    return True

print(ispowerof2(n))