import itertools

arr = [int(input()) for i in range(9)]
l = list(itertools.combinations(arr, 7))
for sumation in l:
    if sum(sumation) == 100:
        for ans in sorted(sumation):
            print(ans)