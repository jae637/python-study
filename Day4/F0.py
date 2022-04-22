N = int(input())
arr = input().split()

d = {k: '' for k in arr}

for idx, x in enumerate(arr, 1):
    d[x] = d[x] + str(idx) + " "

print('unique') if len(arr) == len(d) else print(
    *[f'{k} {v}' for k, v in d.items() if len(v) != 2], sep='\n')
