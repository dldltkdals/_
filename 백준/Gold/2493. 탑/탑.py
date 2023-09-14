'''
#시작시간 :16:21
5
6 9 5 7 4
 
'''
from collections import deque
N = int(input())
towers = list(map(int,input().split(" ")))
q = deque([[towers[0],0]])
dp = [0]*N

for i in range(N):
    
    while q:
        
        if q[-1][0] > towers[i]:
            
            dp[i] = q[-1][1]+1
            break
        else:
            q.pop()
    q.append([towers[i],i])
result = " ".join(map(str,dp))
print(result)
            
        

        
        
    

