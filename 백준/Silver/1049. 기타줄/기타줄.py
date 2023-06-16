#N: 끊어진 기타줄 개수
#ㅡ 기타줄 브랜드
N,M = list(map(int,input().split()))
#prices[i][0]: 6개 패키지 가격
#prices[i][1]: 1개 낱개 가격

prices = [list(map(int,input().split())) for _ in range(M)]
dp = [0]*(N+1)
dp[1] = float('INF')
for i in range(M):
    dp[1] = min(dp[1],prices[i][1])
    single_min = dp[1]
package_min = min(prices)[0]
for i in range(1,N+1):
    if i <= 6:
        dp[i] = min(dp[i-1] + single_min,package_min)
    else:
        dp[i] = min(dp[i-1] + single_min,dp[i-6] + package_min)
    
print(dp[-1])