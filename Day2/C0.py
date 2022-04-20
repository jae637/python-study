N = int(input())
for i in range(N):
    s = input()
    sr = s[::-1]
    tot = int(s) + int(sr)
    if str(tot) == str(tot)[::-1]: print("YES")
    else: print("NO")
