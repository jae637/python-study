N = int(input())
l = [x for x in range(N - 7, N + 14) if x % 14 == 0]
print(max(l[0], 14))
