"""
https://www.acmicpc.net/problem/16234
시작 시간: 23:18 ->00:01 (43분 소요)
"""
N,L,R = list(map(int,input().split(" ")))

nations = [list(map(int,input().split(" "))) for _ in range(N)]
'''
50 30
20 40
50 * 50 * 50 * 

nation        q 144//7  nation
10 15 20    10 15 20   20 20 20
20 30 25    20 30 25   20 20 20
40 22 10       22      40 20 10
'''
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS(start,visited):
    # visited = [[0]*N for _ in range(N)]
    global flag
    visited[start[0]][start[1]] = 1
    #연방의 인구수
    population = nations[start[0]][start[1]]
    #연방국 수
    count = 1
    #연방국의 좌표
    unions = [start]
    
    q = deque([start])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and L <= abs(nations[nx][ny]-nations[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    count += 1
                    population += nations[nx][ny]
                    unions.append([nx,ny]) 
    
    population = population//count
    for union in unions:
        x,y = union
        nations[x][y] = population
    # 연방국이 두나라 이상이면 
    if count > 1:
        flag = True

flag  = True
day = -1
while flag:
    visited = [[0]*N for _ in range(N)]
    day += 1
    flag = False
    BFS([0,0],visited)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS([i,j],visited)
                     
                     
                     
                    
print(day)