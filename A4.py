a = input().split()
b = input().split()
c = input()

dic ={}

for i in range(len(a)):
    dic[a[i]]=b[i]

print(dic[c])