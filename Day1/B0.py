N = int(input())
f = N // 300
N %= 300
o = N // 60
N %= 60
t = N // 10
print(f, o, t) if N % 10 == 0 else print(-1)
