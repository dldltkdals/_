N = int(input())
wine = [0]+[int(input()) for _ in range(N)]

dp = [0]*(N+1)
dp[1] = wine[1]
# print(wine)

for i in range(2,N+1):
    if i == 2:
        dp[i] = dp[i-1] + wine[i]
    else:
        dp[i] = max(dp[i-2] + wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1])
# print(dp)
print(max(dp))