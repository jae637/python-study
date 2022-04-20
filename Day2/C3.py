import re

s = input()
l = re.findall('([a-zA-Z]+)([^a-z^A-Z]*)', s)
print((l[0][0][:10][::-1]))