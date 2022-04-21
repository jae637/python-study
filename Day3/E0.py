pos = [['0' for a in range(102)] for x in range(102)]

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    for a in range(A, A + 10):
        for b in range(B, B + 10):
            pos[a][b] = '1'

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if pos[i][j] == '1':
            cnt += len(['0' for x, y in move if pos[i + x][j + y] == '0'])
print(cnt)