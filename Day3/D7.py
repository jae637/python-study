R, C = map(int, input().split())
arr = [
    '0' * (C + 2) if (x == 0 or x == R + 1) else '0' + input() + '0'
    for x in range(R + 2)
]

move = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
cnt, mcnt = 0, 0
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if arr[i][j] == 'o':
            for r, c in move:
                if arr[i + r][j + c] == 'o': cnt += 1
        else:
            tmp = 0
            for r, c in move:
                if arr[i + r][j + c] == 'o': tmp += 1
            mcnt = max(tmp, mcnt)

cnt //= 2

print(cnt + mcnt)
