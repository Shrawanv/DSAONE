
n = int(input())

def palindrome_number(n):
    res = 0
    temp = n
    
    # reversing the number n
    while temp >= 1:
        res = res * 10 + temp % 10 
        temp = temp // 10

    return res == n

print(f'{n} is palindrome number: {palindrome_number(n)}')

