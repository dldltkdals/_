'''
10:43
'''
import sys
from collections import deque
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    W = input().rstrip()
    K = int(input().rstrip())
   
    check = {}
    MinValue = 1000000
    MaxValue = 0
    if K == 1:
        MaxValue,MinValue = 1,1
        print(MinValue,MaxValue)
        
        continue
    for i in range(len(W)):
        if W[i] not in check:
            check[W[i]] = deque([i])
        else:
            check[W[i]].append(i)
            if len(check[W[i]])==K:
                MaxValue = max(MaxValue,i-check[W[i]][0]+1)
                MinValue = min(MinValue,i-check[W[i]][0]+1)
                check[W[i]].popleft()
    if MaxValue:
        print(MinValue,MaxValue)
    else:
        print(-1)
                
            
            
            
        

