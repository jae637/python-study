N, S = input().split()

rank = 0
d = {str(x): [] for x in range(51)}
tmp = ''
for s in S:
    if s == '<':
        if tmp != '': d[str(rank)].append(tmp)
        rank += 1
        tmp = ''
    elif s == '>':
        if tmp != '': d[str(rank)].append(tmp)
        rank -= 1
        tmp = ''
    else:
        tmp += s
print(*[x for x in d[N] if x != ''])
