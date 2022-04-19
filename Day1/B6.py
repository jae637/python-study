l = [[x for x in input().split()] for i in range(5)]
li = [min(float(b) - float(a) - 1, 4) for a, b in l]
li = [max(float(x), 0) for x in li]

if sum(li) <= 5: print(int(sum(li * 10500)))
elif sum(li) >= 15: print(int(sum(li * 9500)))
else: print(int(sum(li) * 10000))
