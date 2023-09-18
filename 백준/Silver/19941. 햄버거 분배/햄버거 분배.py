'''
https://www.acmicpc.net/problem/19941
17:55
'''
from collections import deque
N,K = list(map(int,input().split(" ")))
table = list(input())
h = deque()
c = deque()
result = 0
# print(table)
person = 0
po = [k for k in range(1,K+1)]
ne = [-1*i for i in po]
check = sorted(po+ne)

for i in range(N):
    if table[i] == "P":
        for j in check:
            idx = i+j
            if 0 <= idx < N:
                if table[idx] == "H":
                    result += 1
                    table[idx] = "0"
                    break
        
       
        
        
    
   
   
print(result)