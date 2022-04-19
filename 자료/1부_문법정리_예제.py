# [예제 1-1-1] 하나 입력 받고 타입 변환

##x = input()
##y = int(input())
##z = float(input())
##
##print(x, type(x))
##print(y, type(y))
##print(z, type(z))

# [예제 1-1-2] 공백으로 구분된 여러개 문자열 한줄에 입력 받기

##x, y = input().split()
##print(x, y, type(x), type(y))

# [예제 1-1-3] 공백으로 구분된 타입이 다른 여러 값 한줄에 입력 받기

##x, y, z = input().split()
##y, z = int(y), float(z)
##print(x, y, z, type(x), type(y), type(z))

# [예제 1-1-4] 공백으로 구분된 여러개 문자열 한줄에 입력 받아 list에 담기

##l = input().split()
##print(l, type(l))
##print(len(l), sorted(l))
##print(l[0], l[1], l[-1])

# [예제 1-1-5] 개수가 지정되지 않은 여러개의 정수를 한줄에 입력 받기

##x, y, z = [int(n) for n in input().split()]
##print(x + y + z)

# [예제 1-1-6] 개수가 지정되지 않은 여러개의 정수를 한줄에 입력 받아 list에 담기

##l = [int(n) for n in input().split()]
##print(l, type(l))
##print(len(l), sum(l), max(l), sorted(l))
##print(l[0], l[1], l[-1])

# [예제 1-1-7] N줄의 문자열을 입력 받아 list에 담기

##N = int(input()) 
##l = [input() for i in range(N)]
##print(l)
##print(l[0], type(l[0]))
##print(len(l))

# [예제 1-1-8] N줄의 정수(동일 타입)를 입력 받아 list에 담기

##N = int(input())
##l = [int(input()) for i in range(N)]
##print(l)
##print(l[0], type(l[0]))
##print(len(l))

# [예제 1-1-9] 문자열 여러개씩 N줄(2차원 배열) 받아 2중 list에 담기

##N = int(input()) 
##l = [input().split() for i in range(N)]
##print(l)
##print(l[0], l[0][0])
##print(len(l), len(l[0]))

# [예제 1-1-10] 정수 여러개씩 N줄(2차원 배열) 받아 2중 list에 담기

##N = int(input())
##l = [[int(n) for n in input().split()] for i in range(N)]
##print(l)
##print(l[0], l[0][0], len(l), len(l[0]))

# [예제 1-1-11] print sep, end keyword parameter

##print(10, 20, 30)
##print(10, 20, 30, sep = '$$')
##print('kim', 'lee', sep = ' - ', end = ' => ')
##print('park')

# [예제 1-1-12] unpack argument 전달

##l = [1, 2]
##t = ('kim', 'lee', 'park')
##print(l, t)
##print(l[0], l[1], t[0], t[1], t[2])
##print(*l, *t)

# [예제 1-1-13] format 메서드를 이용한 인쇄

##s1 = '{}, {}'.format(10, 20)
##s2 = '{0} + {0} = {2}'.format(2, 3, 2 + 2)
##s3 = 'a = {a}, b = {b}'.format(a = 10, b = 20)
##print(s1, s2, s3, sep = '\n')

# [예제 1-1-14] format 메서드 형식 지정

##t = (100, 'Hello')
##print('{0:d} 0x{0:x} {0:f} {1:s}'.format(*t))
##print('|{0:5s}|{0:5}|{1:3}|'.format('Hi','Python'))
##print('|{0:5.1f}|{0:05.1f}|'.format(1.23))
##print('|{0:<6}|{0:_^6}|{0:*>6}|'.format('Hi'))
##print('{:,} {:.2%}'.format(1234, 0.245))
##print('{{{}}}'.format(123) )

# [예제 1-1-15] f-prefix를 이용한 다양한 인쇄

##name = 'mono'
##age = 20
##f1 = 11.3456
##
##print(f'{name }, {age-10}')
##print(f'{f1:7.5}')
##print(f'name = {name}')
##print(f'{age:>5}-{age:0>5}')
##print(f'{age:<5}-{age:0^5}')
##print(f'{123456789:,}')
##print(f'{0.125:.2%}')

# [예제 1-2-1] 기본 연산자

##a, b = 10, 3
##print(a ** b, a / b, a //b, a % b)

# [예제 1-2-2] 결과가 True, False인 연산자와 if식

##n = 15
##x, y = [1,3,9], ('kim','lee')
##print(1 in x, 'lee' in y, 9 not in x)
##print(n % 3 == 0, n % 3 != 0, not n % 3)
##print(n % 2 == 0 and n % 3 == 0, not n % 3 or not n % 5)
##r = 'YES' if n > 10 else 'NO'
##print(r)
##print(n * 2 if n < 10 else 'ERROR')
##print(n * 2) if n < 10 else print('ERROR')

# [예제 1-2-3] sequnece type의 +, * 연산

##print('hi' + 'python', 'hi' * 3)
##x, y = [1,2,3], ['kim','lee']
##print(x + y, x * 2, sep = '\n')
##l = [0] * 3
##print(l)
##l[0] = 100
##print(l)

# [예제 1-2-4] sequnece type의 slicing 연산

##s = 'Hello'
##print(s[:],s[1:3],s[1::2],s[::-1],s[-3:-1],sep = '\n')
##l = [10,20,-40,9,8]
##print(l[:],l[1:3],l[1::2],l[::-1],l[-3:-1],sep = '\n')
##l[1:4] = [-1,'kim', 3.14]
##print(l)
##l[::2] = 'ABC'
##print(l)

# [예제 1-2-5] tuple을 이용한 Lookup Table

##n = 10
##print('HIGH' if n >= 0 else 'LOW')
##t = ('LOW', 'HIGH')
##print(t[n >= 10])
##d = {False : 'LOW', True : 'HIGH'}
##print(d[n >= 10])

# [예제 1-2-6] dict를 이용한 Lookup Table

##s = input()
##print(-1 if s == '가위' else 0 if s == '바위' else 1)
##d = {'가위':-1, '바위':0, '보':1}
##print(d[s])

# [예제 1-2-7] container 타입 변환

##t = tuple([10,3.14,'kim'])
##l = list((10,3.14,'kim'))
##s = set((10,'kim',3.14,10,'kim'))
##d = dict([(1,10),['kim',-1],(100,'A')])
##print(t, l, s, d, sep = '\n')
##print(t[0], l[-1], d[100])
         
# [예제 1-2-8] zip 함수와 dict 변환에 의한 lookup table 생성

##name = ('kim', 'lee', 'park')
##score = [100, 80, 95]
##z = zip(name, score)
##print(*z)
##d = dict(zip(name, score))
##print(d, d['lee'])

# [예제 1-2-9] 주요 Built-in 함수

##print(abs(-3), abs(-3.14), pow(10,2), divmod(10,3))
##x = (10, -2, 27, 9)
##print(len(x), min(x), max(x), sum(x), sorted(x))
##x = ['kim', 'kang', 'ki']
##print(len(x), min(x), max(x), sorted(x))
##print(sorted(x, reverse = True))
##print(all([100,-1,0]),all([100,'kim']))
##print(any((0,0.0,[])),any([1,2,0]))

# [예제 1-2-10] range 함수

##r = range(5)
##print(r, *r)
##print(r[1], r[1:3])
##print(max(r), len(r))
##print(*range(2,5))
##print(*range(2,8,2))
##print(*range(10,3,-2))

# [예제 1-3-1] Sequence 타입 메서드

##t = (1, 10, 3, 90, 8, 3)
##print(t.index(100))
##print(t.index(3), t.index(3, 1), t.index(3, 3), t.index(3, 3, 6))
##print(t.index(min(t)), t.index(max(t)), t.count(3))
##p1 = t.index(3)
##p2 = t.index(3, p1 + 1)
##print(p1, p2)

# [예제 1-3-2] list 메서드 1

##l = [1,2]
##l.append('kim')
##l.append((3.14, 100))
##print(l)
##l.extend((-2, 'A'))
##print(l)
##l.insert(1, -1)
##l.insert(-1, -3)
##print(l)

# [예제 1-3-3] list 메서드 2

##l = [5,3,8,2]
##l.reverse()
##print(l)
##l.sort()
##print(l)
##l.sort(reverse = True)
##print(l)
##
##x = l.pop()
##print(x, l)
##l.remove(3)
##del l[0]
##print(l)
##l.clear()
##print(l)

# [예제 1-3-4] set 동작과 연산

##t = (1, 3, 5, 5, 7, 9)
##l = [1, 3, 3, 8]
##print(set(t), len(set(t)))
##print(set(t) & set(l))
##print(set(t) | set(l))
##print(set(t) - set(l))
##print(set(t) ^ set(l))
##s = {1,2}
##s.add(-1)
##print(s)

# [예제 1-3-5] dict 동작과 연산

##d = {'a' : 10, 'b' : 20}
##print(d['a'])
##print(d['c'])
##print(d.get('a'), d.get('c'), d.get('a', 0))
##d['a'] = -1
##d['d'] = -2
##print(d)
##d.setdefault('b', -3)
##d.setdefault('e', -4)
##print(d)
##x = d.pop('b')
##y = d.pop('f', 0)
##print(x, y, d)

# [예제 1-3-6] 특정 값으로 초기화된 dict 생성

##d1 = dict.fromkeys(['a','b',10])
##d2 = dict.fromkeys(('x','y'), 0)  
##d3 = dict.fromkeys('ABC', 'hi')
##print(d1, d2, d3, sep = '\n')

# [예제 1-3-7] str 메서드 1/2

##s1 = 'Hello Hello'
##print(s1.upper())
##print(s1.lower())
##print(s1.swapcase())
##print(s1.replace('He', 'She'))
##print(s1.replace('ll', '---', 1))
##print(s1.index('ll'))
##print(s1.index('ll', 3))
##print(s1.find('ll'))
##print(s1.count('ll'))
##
##s2 = 'Hello'
##print(s2.split('e'))
##print(s2.split('l'))
##s3 = ' Hi Low '      # 공백 하나씩
##print(s3.split())   
##print(s3.split(' ')) # 공백 하나
##s4 = '  Hi  Low  '   # 공백 두개씩
##print(s4.split())
##print(s4.split(' ')) # 공백 하나
##
##s5 ='    Hello Python  '
##print(s5.strip())
##print(s5.rstrip())
##print(s5.lstrip())
##
##s6 ='aabbcaxb?bxacbbaa'
##print(s6.strip('axb?'))
##print(s6.rstrip('axb?'))
##print(s6.lstrip('axb?'))

# [예제 1-3-8] str 메서드 2/2

##s ='aabbcaxb?bxacbbaa'
##print(s.startswith('aab'), s.startswith('abb'))
##print(s.endswith('baa'), s.endswith('bba'))
##
##print('A B5CD!'.isupper(), 'A b5cD!'.islower())
##print('AbC'.isalpha(), 'AbC1'.isalpha())
##print('aA123'.isalnum(), 'a#123'.isalnum())
##print('12'.isdecimal(), '12A'.isdecimal())

# [예제 1-3-9] 문장 전처리 예

##s = ('   Hi   python   ', 'Good  \t Day~', '   Thank you   ')
##y = [' '.join(x.split()) for x in s]
##r = '\n'.join(y)
##print(r)

# [예제 1-4-1] 사용자 함수 설계

##def f1() :
##    print('f1')
##
##f1()
##
##def f2(a, b) :
##    c = a + b
##    print(a, b, c)
##    return c
##
##print(f2(3,4))
##
##def f3(a, b) :
##    return a // b, a % b
##
##a, b = f3(10,3)
##print(a, b)
##print(f3(10,3))

# [예제 1-4-2] 전역변수 공유

###[1]
##
##def f1() :
##    cnt += 1
##
##cnt = 0
##f1()
##f1()
##print(cnt)

###[2]
##
##def f2() :
##    global cnt
##    cnt += 1
##
##cnt = 0
##f2()
##f2()
##print(cnt)

# [예제 1-4-3] Lambda Expression

##f1 = lambda : 10
##f2 = lambda a, b : a + b
##f3 = lambda a, b : (a // b, a % b)
##print(f1(), f2(3, 4), f3(10, 3), sep = '\n')

# [예제 1-4-4] Lambda Expression 활용 예

##x = map(int, ('10', '20', '30'))
##print(sum(x))
##
##def func(n) :
##    return n ** 2
##
##x = map(func, [3, 5, 10])
##print(*x)
##
##x = map(lambda n : n ** 2, [3, 5, 10])
##print(*x)

# [예제 1-4-5]

##def func(y) :
##    print(y, y[1])
##    return y[1]
##
##x = [(21, 'song'), (28, 'kim'), (19, 'kim')]
##print(min(x), max(x), sorted(x), sep = '\n')
##print(min(x, key = func))
##print(min(x, key = lambda y : y[1]))
##print(min(x, key = lambda y : (y[1], y[0])))
##print(sorted(x, key = lambda y : (y[1], y[0])))
##print(sorted(x, key = lambda y : (y[1], -y[0])))

# [예제 1-5-1] map과 list compprehension

##x = ['10', '34', '-27', '9']
##y = map(lambda n : int(n) * 2, x)
##print(y)
##print(type(y), *y)
##z = [int(n) * 2 for n in x]
##print(z)

# [예제 1-5-2] filter와 list compprehension

##x = [10, 34, -27, 9]
##y = filter(lambda n : n % 2 == 0, x)
##print(y)
##print(type(y), *y)
##z = [n for n in x if n % 2 == 0]
##print(z)

# [예제 1-5-3] comprehension의 장점

##x = [10, 34, -27, 9]
##y = filter(lambda n : n % 2 == 0, x)
##z1 = list(map(lambda n : n ** 2, y))
##print(z1)
##z2 = [n ** 2 for n in x if n % 2 == 0]
##print(z2)

# [예제 1-5-4] list 생성

##l1 = [0] * 3
##l1[0] = 100
##print(l1)
##
##l2 = [[0] * 3] * 2
##l2[0][0] = 100
##print(l2)
##
##l3 = [0 for i in range(3)]
##l3[0] = 100
##print(l3)
##
##l4 = [[0 for i in range(3)] for j in range(2)]
##l4[0][0] = 100
##print(l4)
##
##l5 = [[0] * 3 for j in range(2)]
##l5[0][0] = 100
##print(l5)

# [예제 1-5-5] comprehension 활용

##l1 = [[] for i in range(3)]
##print(l1)
##
##t = ((1,5),(9,0,-1,7),(8,2,1))
##m = min([min(x) for x in t])
##s = sum([sum(x) for x in t])
##print(m, s)
##
##l = [y for x in t for y in x]
##print(l)
##print(min(l), sum(l))

# [예제 1-5-6] set, dict comprehensions

##t = (1, 3, -1, 2, -2, 3)
##s = {x ** 2 for x in t}
##print(s)
##
##x, y = (1,3)
##print(x, y)
##x, y, *z = (1,3,6,2)
##print(x, y, z)
##x, *y, z = (1,3,6,2)
##print(x, y, z)
##
##l = [('kim',21), ('lee',30), ('park',29)]
##d = {k : v for v, k in l if k > 25}
##print(d)
##
##x = ('kim','lee','park')
##e = tuple(enumerate(x))
##print(e)
##d1 = {k : v for k, v in enumerate(x, 10)}
##print(d1)
##d2 = {k : 0 for k in x}
##print(d2)

# [예제 1-6-1] if 문

##a = 6
##
##if a % 2 == 0 :
##    print(2)
##if a % 3 == 0 :
##    print(3)
##if a % 6 == 0 :
##    print(6)
##
##if a % 2 == 0 :
##    print(2)
##elif a % 3 == 0 :
##    print(3)
##elif a % 6 == 0 :
##    print(6)
##else :
##    print(0)

# [예제 1-6-2] for 문

##t = ('kim', 'lee', 'park')
##
##for i in range(len(t)) :
##    print(t[i])
##
##for x in t :
##    print(x)
##
##for i, x in enumerate(t) :
##    print(i, x)

# [예제 1-6-3] 2중 for 문

##t = ((1,8,3),(5,6))
##
##for i in range(len(t)) :
##    for j in range(len(t[i])) :
##        print(t[i][j], end = ' ')
##
##for i in range(len(t)) :
##    for x in t[i] :
##        print(x, end = ' ')
##
##for x in t :
##    for y in x :
##        print(y, end = ' ')

# [예제 1-6-4] break, continue, else

##t = (1, 5, 4, 7, 6, 7)
##
##for x in t :
##    if x % 3 == 0 :
##        break
##    if x % 2 == 0:
##        continue
##    print(x)
##
##for x in t :
##    if x >10 :
##        break
##    print(x)
##else :
##    print('else:', x)
    
# [예제 1-6-5] for 문의 단점

##t = ('KIM','Hi','low')
##r1 = list(filter(lambda x : x.isupper(), t))
##print(len(r1), r1)
##r2 = [x for x in t if x.isupper()]
##print(len(r2), r2)
##
##r3 = []
##for x in t :
##    if x.isupper() :
##        r3.append(x)
##print(len(r3), r3)

# [예제 1-6-6] for가 유용한 경우

##s = 0
##for x in (1,5,9) :
##    s += x
##print(s)
##
##r1 = [i for i in range(10) if i % 2]
##r1 = r1[:3]
##print(r1)
##
##r2 = []
##for i in range(20) :
##    if i % 2 :
##        r2.append(i)
##        if len(r2) == 3 :
##            break
##print(r2)
##
##b1, b2 = [], []
##
##for i in range(10) :
##    if i % 2 :
##        b1.append(i)
##    if i % 3 :
##        b2.append(i)
##print(b1, b2, sep = '\n')
