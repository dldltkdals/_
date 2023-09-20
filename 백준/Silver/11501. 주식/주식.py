'''
시작 시간: 10:30
'''
from collections import deque
def Trade(N,chart):

    chart = chart[::-1]
    profit = 0
    Max = chart[0]
    for i in range(1,N):
        if chart[i] > Max:
            Max = chart[i]
        else:
            profit += (Max-chart[i])
    print(profit)
T = int(input())
for _ in range(T):
    N = int(input())
    chart = list(map(int,input().split(" ")))
    Trade(N,chart)