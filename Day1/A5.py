i = [int(item) for item in input().split()]
 
dic ={}
for start in range(1,i[0]+1,2):
    tmp =[]
    for count in range(2):
        tmp.append(start+count)
    for count in range(2):
        tmp.append(i[0]-start-count+1)
    dic[start]=tmp
    dic[start+1]=tmp
 
tmpdic = dic[i[1]]
tmpdic.remove(i[1])
tmpdic.sort()
print(*tmpdic)