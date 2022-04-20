N = int(input())
arr = []
for i in range(N):
    s = int(input())
    m = str(s)
    while len(m) > 1:
        num = sum([int(x) for x in m])
        m = str(num)
    arr.append([s, int(m)])
print(arr)
print(max(arr, key=lambda x: (x[1], -x[0]))[0])
