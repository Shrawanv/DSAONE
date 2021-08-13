
def sieve_prime(n):
    prime = [True for i in range(n+1)]
    for i in range(2,n):
        if prime[i] == True:
            j = i*i
            while j <= n:
                prime[j] = False
                j += i

    for i in range(2,n):
        if prime[i] == True:
            print(i,end=' ')

if __name__ == '__main__':
    sieve_prime(int(input()))
