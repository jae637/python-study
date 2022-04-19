l = [float(i) for i in input().split()]
l.sort(key=lambda x: abs(3.5 - x))
print('{:.6f} {:.6f}'.format(l[0], l[4]))
# print(f'{l[0]:f},{l[4]:f}')