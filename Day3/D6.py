N = int(input())
l = [[int(x) for x in input().split()] for a in range(N)]
rs = [sum(i) for i in l]
rsi = rs.index(max(rs))
cs = [sum(a) for a in zip(*l)]
csi = cs.index(max(cs))
print(rsi + 1, csi + 1)
