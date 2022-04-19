N = int(input())
l = [int(x) for x in input().split()]
li = [[idx, x] for idx, x in enumerate(l, 1)]
sl = sorted(li, key=lambda x: (-x[0], x[1]))
print(sl[0][1], sl[1][1], sl[2][1])
