import math

N = int(input())
l = [float(input()) / float(10) for x in range(N)]
times = [math.ceil(x) for x in l if x >= 1]
prices = [500 if t < 3 else 500 + (t - 3) * 300 for t in times]
print(sum(prices))