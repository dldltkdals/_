T = int(input())

num = [int(input()) for _ in range(T)]
N = max(num)
dp = [[0]*4 for _ in range(N+3)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1

for i in range(2,N+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) %1000000009
    if i > 2:
        dp[i][2] = (dp[i-2][1] + dp[i-2][3])%1000000009
    if i > 3:
        dp[i][3] = (dp[i-3][2] + dp[i-3][1])%1000000009
for i in num:
    print(sum(dp[i])%1000000009)

