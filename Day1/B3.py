K = int(input())
N = int(input())
l = [input().split() for x in range(N)]
l = [(int(x[0]), x[1]) for x in l]
time = 0
for i in range(len(l)):
    time += l[i][0]
    if time > 210:
        break
    if (l[i][1] == 'T'):
        K += 1
print(8 if K % 8 == 0 else K % 8)
