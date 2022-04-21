N = int(input())
arr = [[int(x) for x in input().split()] for i in range(N)]
turn = (int(input()) // 90) % 4

for i in range(turn):
    arr = [x[::-1] for x in zip(*arr)]
for x in arr:
    print(*x)
