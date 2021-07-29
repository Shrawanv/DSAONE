import math as m

n = int(input('enter n value: '))

res = []
for i in range(1,m.floor(m.sqrt(n))):
    if n % i == 0:
        res.append(i)
        if i != m.sqrt(n):
            res.append(n//i)

print(sorted(res))
