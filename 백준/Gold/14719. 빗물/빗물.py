'''
https://www.acmicpc.net/problem/14719
시작시간 15:28
'''

H,W = list(map(int,input().split(" ")))
buildings = list(map(int,input().split(" ")))

result = 0
HightMax,MaxIdx = buildings[0],0
if W <= 2:
    print(0)
    exit()
LMax,RMax = max(buildings[0],buildings[1]),max(buildings[2:])
for i in range(1,W-1):
    if buildings[i]>= LMax or buildings[i] >= RMax:
        LMax = buildings[i]
        RMax = max(buildings[i+1:])
        
    else: 
        result += max(min(LMax,RMax)-buildings[i],0)
    # print(i,result,LMax,RMax)
print(result)