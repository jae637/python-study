import sys

readl = sys.stdin.readline  # 속도 개선
n = int(readl())
narr = dict([readl().split() for i in range(n)])
m = int(readl())
marr = [readl().rstrip() for i in range(m)]  #오른쪽 공백 자르기
s = [narr[x] if narr.get(x) else x for x in marr]
print(''.join(s))