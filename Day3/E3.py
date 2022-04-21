N = int(input())
mother = [input() for _ in range(N)]
M = int(input())
pattern = [input() for _ in range(M)]

cnt = 0
for i in range(N - M + 1):
    for j in range(N - M + 1):
        flag = True
        for ii in range(M):
            for jj in range(M):
                if mother[i + ii][j + jj] != pattern[ii][jj]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            cnt += 1
print(cnt)
