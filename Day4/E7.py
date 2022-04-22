from collections import Counter

s = input()
s = sorted([x for x in s if x.islower()])
c = Counter(s).most_common(1)
print(c[0][0])