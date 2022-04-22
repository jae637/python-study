S, T = input().split()
T = int(T)

flag = True
s = len(S)
for i in range(1, len(S)):
    A = int(S[:i])
    B = int(S[i:s])
    if A + B == T:
        print(str(A) + "+" + str(B) + "=" + str(T))
        flag = False
        break
if flag:
    print("NONE")
