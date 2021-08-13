# 4 = 2 + 2


def prime_nums(n):
    sieve = [True for i in range(n+1)]
    for i in range(n):
        if sieve[i] == True:
            j = i*i
            while j <=n:
                sieve[j] = False
                j += 1
    for i in range(2,n):
        if sieve[i] == True:
            print(i)



            
 