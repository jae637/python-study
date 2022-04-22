s = input()
cnt = [0, 0]
for i in range(0, len(s)):
    if s[i:i + 3] == 'KOI':
        cnt[0] += 1
    if s[i:i + 3] == 'IOI':
        cnt[1] += 1
print(*cnt, sep='\n')
