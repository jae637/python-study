l = input().split()
clock = min([
    l[i % 4] + l[(i + 1) % 4] + l[(i + 2) % 4] + l[(i + 3) % 4]
    for i in range(4)
])
all = sorted(
    set([
        min([
            str(x)[a % 4] + str(x)[(a + 1) % 4] + str(x)[(a + 2) % 4] +
            str(x)[(a + 3) % 4] for a in range(4)
        ]) for x in range(1111,
                          int(clock) + 1) if '0' not in str(x)
    ]))
print(all.index(clock) + 1)
