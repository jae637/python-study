arr = [[int(x) for x in input().split()] for i in range(int(input()))]
arr1 = [b % a for a, b in arr]
print(sum(arr1))
