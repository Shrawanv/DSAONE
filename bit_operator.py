# AND operator
# AND ( & ) operator return 1 if both bits are 1
# print(0 & 0) # returns 0
# print(0 & 1) # returns 0
# print(1 & 1) # returns 1

# OR operator
# OR ( | ) operator returns 1 of any of the bit is 1
# print(0 | 0) # returns 0
# print(0 | 1) # returns 1 
# print(1 | 1) # returns 1

# # XOR operator
# # XOR ( ^ ) operator returns 1 if both the bit is different
# print(0 ^ 0) # returns 0
# print(0 ^ 1) # returns 1
# print(1 ^ 1) # returns 0

 

n = int(input("enter number: "))

# a = time.time()
def prime_fun(n):  
    if n & 1 == 0:
        print('number is prime')
    else:
        print('number is not prime')
# b = time.time()

# c = time.time()
def my_prime_fun(n):
    if n % 2 == 0:
        print('number is prime')
    else:
        print('number is not prime')   
# d = time.time()



# print(f'bit function {b-a}')
# print(f'non_bit function {d-c}')

print(my_prime_fun(n))

