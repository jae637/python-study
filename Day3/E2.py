arr = [[int(x) for x in input().split()] for _ in range(4)]
total = [sum(x) for x in zip(*arr)]
print(total.index(min(total)))
