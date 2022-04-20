X, Y = input().split()
A = [X[i] for i in range(4) if X[i] == Y[i]]
B = [X[i] for i in range(4) for j in range(4) if i != j and X[i] == Y[j]]
print(f'{len(A)}A{len(B)}B')