from collections import Counter

while True:
    tmp = input()
    if tmp == 'END': break
    d = dict(Counter(sorted(tmp.split())))
    print('\n'.join([k + " : " + str(v) for k, v in d.items()]))