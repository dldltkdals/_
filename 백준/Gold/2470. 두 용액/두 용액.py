N = int(input())
liq = list(map(int,input().split(" ")))
liq.sort()
s = 0
e = N - 1
minValue = float("inf")
minSIdx = s
minEIdx = e
while s != e:
    temp = liq[s] + liq[e]
    if abs(temp) <= minValue:
        minValue = abs(temp)
        minSIdx = s
        minEIdx = e
    if temp < 0:
        s += 1
    else:
        e -= 1
print(liq[minSIdx],liq[minEIdx])
    