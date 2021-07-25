dividend = int(input('dividend: '))
divisor = int(input('divisor: '))

'''Regular Method'''
# def divide_integers(dividend:int, divisor:int) ->int:
#     quotient = 0
#     while dividend >= divisor:
#         quotient += 1
#         dividend -= divisor 

#     return f'quotient: {quotient}\nRemainder: {dividend}'

# print(divide_integers(dividend, divisor))

'''Using Bit Manipulation'''

def divide_integer(dividend:int, divisor:int) -> int:
    ans = 0
    i = 0
    while divisor <= dividend:
        divisor << i
        ans += 1 << i
        i += 1

    return ans

print(divide_integer(dividend, divisor))