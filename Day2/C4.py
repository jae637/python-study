import re

a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
idx = a.find(s.lower())
l = re.findall('([a-z]*)([A-Z]*)', s)
if idx == -1: print('Error')
elif l[0][0] != '': print(a[:idx + 1])
else: print(a[idx:].upper())
