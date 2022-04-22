N = int(input())
d = {
    i / j: str(i) + "/" + str(j)
    for i in range(N, -1, -1) for j in range(N, 0, -1) if i / j <= 1
}
sl = sorted(d.items(), key=lambda item: item[0])
print(*[a[1] for a in sl])
