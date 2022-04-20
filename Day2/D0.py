import itertools


def minmax(s):
    mn = ''.join(sorted(s))
    mx = ''.join(sorted(s,reverse=True))
    return int(mn), int(mx)


N = input()
ans = 0
while True:
    if N == '6174': break
    mn, mx = minmax(N)
    N = str(mx - mn)
    ans += 1
print(ans)