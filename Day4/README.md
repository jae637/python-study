# Day4

## 1,2 교시
문제 풀이
## 3교시
- Collections
  - Counter
    - 해당 string 의 갯수를 dictionary 형태로(dic 아님) 리턴해줌 (Counter Class)
    ```python
    from collections import Counter

    s = input()  # aaaabbcceeddaaaddd
    s = sorted([x for x in s if x.islower()])
    c = Counter(s).most_common(1) # 인자가 없을 때 : 내림차순 정렬, 있을 때 : 갯수만큼 내림차순
    print(c) # [('a', 7)]
    print(c[0][0])
    ```
## 4교시
- sys
  ```python
  import sys

  readl = sys.stdin.readline # 속도 개선
  n= int(readl())
  narr = [readl().split() for i in range(n)]
  m = int(readl())
  marr = [readl().rstrip() for i in range(m)] #오른쪽 공백 자르기
  ```
## 점심시간
## 5, 6교시
문제 풀이
## 7교시
- Queue
  - BFS를 풀기 위해선 반드시 Queue를 사용할 수 있어야 함
## 문제 List
| 문제번호| 제목|
|-------|-------|
| E5|	[2-7-기본1]분수 정렬|
| E6|	[2-7-응용1]가장 많은 알파벳은?|
| E7|	[2-7-응용2]가장 많은 알파벳은? (collections 활용 재설계)|
| E8|	[2-7-실전1]문자열 변환		|
|E9	|[2-7-실전2]단어 세기|
| F0	|[2-7-실전3]UNIQUENESS|