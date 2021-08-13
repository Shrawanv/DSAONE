def dist_circle(A,B,C):
    res = (C + A -1) % B
    if res == 0:
        return B 
    return res

A = int(input())
B = int(input())
C = int(input())

print(dist_circle(A,B,C))