N,P = [int(x) for x in input().split()]

a= P+1 if P%2 else P-1
b,c =N-a+1,N-P+1
sol = sorted([a,b,c])
print(*sol) 