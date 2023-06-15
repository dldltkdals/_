T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0]*(N+1) for _ in range(2)]
    sticker = [[0] + list(map(int,input().split())) for _ in range(2)]
    dp[0][1],dp[1][1] = sticker[0][1],sticker[1][1]

    for i in range(2,N+1):
        for j in range(2):
            dp[j][i] = max(dp[j-1][i-1],dp[j][i-2],dp[j-1][i-2]) + sticker[j][i]
       

    print(max(max(dp[0]),max(dp[1])))

    