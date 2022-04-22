from collections import deque

M, N = map(int, input().split())
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def inbound(x, y):
    return x < N and x >= 0 and y < M and y >= 0


arr = [input().split() for x in range(N)]
q = deque([(a, b, 0) for a in range(N) for b in range(M) if arr[a][b] == '1'])
while len(q) != 0:
    l = q.pop(0)
    tmppos = [(l[0] + x, l[1] + y, l[2] + 1) for x, y in move
              if inbound(l[0] + x, l[1] + y)]
    for a, b, c in tmppos:
        if arr[a][b] == '0':
            arr[a][b] = c
            q.append((a, b, c))

print(max([max([int(a) for a in x])
           for x in arr])) if sum([x.count('0')
                                   for x in arr]) == 0 else print(-1)
