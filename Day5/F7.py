N, K = map(int, input().split())

a = N // 4
s = input() * 2
l = set([s[a * i + j:a * (i + 1) + j] for i in range(a + 1) for j in range(a)])
l = sorted([int(item, 16) for item in l], reverse=True)
print(l[K - 1])
