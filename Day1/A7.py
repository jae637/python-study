N = int(input())
sum=0
for i in range(N):
    a,b=[int(i) for i in input().split()]
    sum+=b%a
print(sum)
