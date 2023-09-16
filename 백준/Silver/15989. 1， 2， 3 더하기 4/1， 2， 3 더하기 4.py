'''
https://www.acmicpc.net/problem/15989
17:33

1 1 -> 1
2 1+1,2 -> 2
3 1+1+1,1+2,3 -> 3
4 1+1+1+1,1+1+1+2,2+2, 1+3 -> 4
5 1+1+1+1+1,1+1+1+2, 1+2+2,1+1+3,2+3-> 5






'''
T = int(input())

dp = [1]*(10001)
for i in range(2,10001):
    dp[i] += dp[i-2]
for i in range(3,10001):
    dp[i] += dp[i-3]
 
 
 
for _ in range(T):
    N = int(input())

        
        
    print(dp[N])
