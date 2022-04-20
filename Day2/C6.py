N = int(input())
l = [input() for x in range(N)]
for item in l:
    tmp = item[::-1]
    if tmp in l:
        print(len(tmp), tmp[len(tmp) // 2])
        break
