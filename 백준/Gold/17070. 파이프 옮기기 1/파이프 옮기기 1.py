'''
그래프 탐색이 종료될 조건

1. 벽에 닿을때
2. N,N에 도달할때


h: 가로
v: 수직
t: 회전

!!!!!!!!: 해당문제는 사이클이 안생기기 때문에 방문한 곳을 체크하지 않아도 무한 루프가 안생긴다!!!!!
'''
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

house = [sys.stdin.readline().rstrip().split() for _ in range(N)]
q= deque([[[0,1],"h"]])# 파이프의 끝 좌표, h: 가로 방향
if house[N-1][N-1] == "1":
    print(0)
    exit()

move = {"h":[0,1],"v":[1,0],"t":[1,1]}
state_move = {"h":["h","t"],"v":["v","t"],"t":["h","v","t"]}
count = 0
while q:
    temp, state = q.pop()
    x,y = temp

    for s in state_move[state]: 
        nx = x + move[s][0]
        ny = y + move[s][1]
        if 0 <= nx < N and 0 <= ny < N:
            if s == "t":
                if house[nx-1][ny] == "1" or house[nx][ny-1] == "1":
                    break
            if house[nx][ny] == "0":
                if nx == N-1 and ny == N-1:
                    count += 1
                    continue
                q.append([[nx,ny],s])
    

        
print(count)
