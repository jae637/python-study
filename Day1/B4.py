base = ''
height = 0
for c in input()
    height += 5
    if base != c:
        height += 5
    base = c
print(height)
