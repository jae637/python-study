s = input().lower()
alpha = 'abcdefghijklmnopqrstuvwxzy'
d = {x: s.count(x) for x in alpha}
print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0])
