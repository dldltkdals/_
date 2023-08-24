from collections import deque
L,C = map(int,input().split())
alpha = sorted(list(input().split()))
#모음들의 집합
vowel_check = {"a","e","i","o","u"}
#가능성 있는 암호를 담을 리스트
code = []
password = deque([])

def dfs(idx,vo):
    # vo: 모음의 개수
    
    if len(password) == L:
        #만약 모음이 존재하고 (and) 전체 길이에서 모음 갯수를 뺀(자음의 갯수)가 2 이상일때
        if vo:
            if (L-vo) >= 2:
                print("".join(list(password)))
        return
  
    for i in range(idx,C):
        char = alpha[i]
        if char in vowel_check:
            vo += 1
        password.append(char)
        dfs(i+1,vo)
        password.pop()
        if char in vowel_check:
            vo -= 1
dfs(0,0)