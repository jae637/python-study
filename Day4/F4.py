M, N = map(int, input().split())


def inbound(x, y):
    return x < N and x >= 0 and y < M and y >= 0


arr = [list(input()) for x in range(N)]
sy, sx = map(lambda x: int(x) - 1, input().split())
arr[sx][sy] = "3"
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

mx = 3
q = [(sx, sy, 3)]
while len(q) != 0:
    l = q.pop(0)
    tmppos = [(l[0] + x, l[1] + y, l[2] + 1) for x, y in move
              if inbound(l[0] + x, l[1] + y)]
    for a, b, c in tmppos:
        if arr[a][b] == '1':
            arr[a][b] = c
            q.append((a, b, c))
            mx = max(mx, c)

print(mx, sum([x.count('1') for x in arr]), sep='\n')
