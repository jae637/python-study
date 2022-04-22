N = int(input())
ans = 0
for i in range(N):
    M, k = input().split()
    if (len(set(k)) != len(k) or len(set(M)) != len(M)):
        ans += 1
        continue
    l = [c for c in k if M.find(c) != -1]
    if len(l) > 2: ans += 1
print(ans)