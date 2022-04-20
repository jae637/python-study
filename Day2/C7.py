import re

M = input()
s = input()
sett = set(s)
sett = [x + '{' + M + ',' + str(len(s)) + '}' for x in sett]
rs = re.findall('|'.join(sett), s)
rs.sort(key=lambda x: -len(x))
print(rs)
for rep in rs:
    s = s.replace(rep, rep[0] + '(' + str(len(rep)) + ')')
print(s)