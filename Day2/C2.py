import re

s = input()
l = re.findall('([^.! ]+)([.!]*)', s)
ans = [x[0][::-1].upper() + x[1] for x in l]
print(" ".join(ans))