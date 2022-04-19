a, b = input().split()
l = [int(i) for i in input().split()]
l.sort()
size = 0
count = 0
for item in l:
    size += item
    if size > int(b):
        break
    count += 1
print(count)