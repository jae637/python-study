l = [[x for x in input().split()] for i in range(4)]
li = [int(x[1]) - int(x[0]) for x in l]
lis = [sum(li[:idx + 1]) for idx in range(len(li))]
print(li, lis)
print(max(lis))
