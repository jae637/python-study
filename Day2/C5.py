import re

TC = int(input())
for i in range(TC):
    M = input()
    S = input()
    if len(re.findall('[' + M + ']+', S)): print('YES')
    else: print("NO")
