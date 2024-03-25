nm = input().split()
n = int(nm[0])
m = int(nm[1])

matrix = [[0]*m for _ in range(n)]
el = 1
right = 0
down = 0
left = 0
up = 0

while el < (m*n)+1:
    for j in range(right, m):
        if matrix[right][j] == 0:
            matrix[right][j] = el
            el = el+1
        else:
            continue
    right = right+1
    for l in range(down, n):
        if matrix[l][-down-1] == 0:
            matrix[l][-down-1] = el
            el = el+1
        else:
            continue
    down = down+1
    for o in range(left+1, m):
        if matrix[-left-1][-o-1] == 0:
            matrix[-left-1][-o-1] = el
            el = el+1
        else:
            continue
    left = left+1
    for p in range(up+1, n):
        if matrix[-p-1][up] == 0:
            matrix[-p-1][up] = el
            el = el+1
        else:
            continue
    up = up+1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
