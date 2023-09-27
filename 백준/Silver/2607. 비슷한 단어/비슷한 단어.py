'''
https://www.acmicpc.net/problem/2607
22:17

자료구조

두 단어가 같은 구성을 갖는 경우,
또는 한 단어에서 한 문자를 더하거나, 빼거나,
하나의 문자를 다른 문자로 바꾸어(swap)
나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들
두 단어를 서로 비슷한 단어라고 한다.
'''
N = int(input())
word = list(input())


result = 0
for _ in range(1,N):
    standard = word[:]
    temp = input()
    count = 0
    for c in temp:
       if c in standard:
           standard.remove(c)
       else:
           count += 1
    if count < 2 and len(standard) < 2:
        result += 1 
print(result)