N = int(input())
l = [int(x) for x in input().split()]
li = [(l[i], i + 1) for i in range(len(l))]
sl = sorted(li, key=lambda x: (-x[0], x[1]))
print(sl[0][1], sl[1][1], sl[2][1])
