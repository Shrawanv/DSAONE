def bishop_move(row,col):
    res = 0
    for i in ([1,1],[1,8],[8,1],[8,8]):
        res += min(abs(row - i[0]), abs(col - i[1]))

    return res

row = int(input())
col = int(input())
print(bishop_move(row,col))