d = {
    int(s): (i, idx)
    for s, idx in enumerate(input().split()) for i in range(5)
}
print(d)
