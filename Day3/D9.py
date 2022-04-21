pos = [['0' for a in range(101)] for x in range(101)]

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    for a in range(A, A + 10):
        for b in range(B, B + 10):
            pos[a][b] = '1'
cnt = 0
for l in pos:
    s = [x for x in l if x == '1']
    cnt += len(s)
print(cnt)