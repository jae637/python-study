M, N = map(int, input().split())


def inbound(x, y):
    return x < N and x >= 0 and y < M and y >= 0


sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
arr = [list(input()) for x in range(N)]
arr[sx][sy] = "1"
cnt = 1
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

q = [(sx, sy, 0)]
while len(q) != 0:
    l = q.pop(0)
    if l[0] == ex and l[1] == ey:
        print(l[2])
        break
    tmppos = [(l[0] + x, l[1] + y, l[2] + 1) for x, y in move
              if inbound(l[0] + x, l[1] + y)]
    for a, b, c in tmppos:
        if a == ex and b == ey:
            print(c)
            q = []
            break
        if arr[a][b] == '0':
            arr[a][b] = '1'
            q.append((a, b, c))
