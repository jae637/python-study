# Day2

## 1교시
문제 풀이
## 2교시
- Sequence Type
  - append
    ```python
      l =[1,2,3]
      l.append("kim")
      # [1,2,3,"kim"]  
    ```
  - extend
    ```python
      l= [1,2,3]
      l.extend((3,4))
      #[1,2,3,3,4]
## 3교시
- str
  - strip
    - 해당되는 항목들을 만나면 제거
    - 앞뒤로 제거하고, 해당되지 않는 항목을 만나면 스톱
  - rstrip
    - right strip
  - lstrip
    - left strip
  - index vs find
    - 같은 기능, 없을 때 error 인지 아닌지 판별
    ```python
    s1= 'Hello Hello'
    s1.index('ll') #2
    s1.index('ll',3) #8
    s1.index('zz') #error
    s1.find('zz') #-1
    ```
  - join
    - 문자열을 합치는데 자주 사용됌
- 정규식
  - 
    - 

## 4교시
문제풀이
## 점심시간
## 5교시 
- Comprehension
  - 2중 포문을 이용한 comprehension
  ```python
  l=[a+i for i in range(4) for a in range(2)] # [0,1,2,3,1,2,3,4]
  ```
## 6,7교시
문제 풀이
## 8교시

## 문제 List
| 문제번호| 제목|
|-------|-------|
|A0|채점시스템 동작 확인용 문제|
| C0	|[2-4-기본1]합의 회문수		|
| C1	|[2-4-응용1]문자열 뒤집기Ⅱ	|
| C2	|[2-4-응용2]문자열 뒤집기Ⅱ |
| C3	|[2-4-실전1]10글자까지만 거꾸로	|
| C4	|[2-4-실전2]문자까지의 문자열		|
| C5	|[2-4-실전3]Two Strings		|
| C6	|[2-4-추가1]해킹		|
| C7	|[2-4-추가2]문자열 압축	|
| C8	|[2-5-기본1]숫자맞추기		|
| C9|	[2-5-응용1]십자카드 문제|
| D0	|[2-5-실전1]6174		|
| D1	|[2-5-실전2]100만들기	|
| D2	|[2-5-실전3]숫자근|