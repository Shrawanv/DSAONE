# no is prime when it is divisible by only itself and 1.
# 1 is not prime number

n = int(input('enter number: '))

def isPrime(n):
    notPrime = 0
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                notPrime = 1
                break
    print(f'debugging: {notPrime}')
    if notPrime:
        print(f'{n} is not prime number')
    else:
        print(f'{n} is prime number')
    
isPrime(n)
