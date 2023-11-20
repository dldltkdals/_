import math
T  = int(input())
for _ in range(T):
    M,N,x,y = list(map(int,input().split(" ")))
    x_hat,y_hat = x,y
    
    while x_hat<=math.lcm(M,N):
        if x_hat > 0 and ((x_hat-y)%N==0):
            print(x_hat)
            break
        x_hat += M
    if (x_hat-y)%N!=0:
        print(-1)

