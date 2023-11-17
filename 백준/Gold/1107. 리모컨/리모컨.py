'''
경우의 수는 네 가지
1. 아무것도 사용안함== target과 currChannel이 같다
2. +, - 로 만 이동
3. 숫자 버튼으로만 이동
4. 숫자, +,- 버튼 모두 사용
'''


target = int(input())
N = int(input())
brokenButton = set()
if N:
    brokenButton = set(list(input().split(" ")))
minPressCount = abs(target-100)
for num in range(1000000):
    num = str(num)
    
    for i in range(len(num)):
        if num[i] in brokenButton:
            break
        if i == (len(num)-1):
            minPressCount = min(minPressCount,len(num)+abs(int(num)-target))
print(minPressCount)
            








    

  


