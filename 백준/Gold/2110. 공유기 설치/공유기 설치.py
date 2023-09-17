'''
https://www.acmicpc.net/problem/2110

14:26
1 2 4 8 9 


'''
N,C = list(map(int,input().split(" ")))

location = sorted([int(input()) for _ in range(N)])
distance = location[-1]-location[0]
srt,end = location[0],location[-1]
flag = 0
while 1:
    curr = location[0]
    router = 1
    for house in location[1:]:
        TempDis = house - curr
        if TempDis >= distance:
            router += 1
            curr = house
    if router < C:
        if flag == 1:
            break
        distance = distance//2
        
    else: # router >= C
        distance += 1
        flag = 1
print(distance-1)