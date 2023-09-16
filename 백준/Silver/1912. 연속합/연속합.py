'''
https://www.acmicpc.net/problem/1912
시작시간 02:22
'''
N = int(input())
numbers = list(map(int,input().split(" ")))
MaxValue = max(numbers)
temp = 0
for i in range(N):
    temp += numbers[i]
    if temp < 0:
        temp = 0
    else:
        if MaxValue < temp:
            MaxValue = temp

print(MaxValue)
    
    