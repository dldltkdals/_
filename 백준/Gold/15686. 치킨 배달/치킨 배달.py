from collections import deque
from itertools import combinations
import sys
N,M = map(int,sys.stdin.readline().split(" "))
board = [list(map(int,sys.stdin.readline().split(" "))) for i in range(N)]
chicken = []
# print(board)
house  = []
return_list = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = float('inf')
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i,j])
        if board[i][j] == 1:
            house.append([i,j])
combin = list(combinations(chicken, M))
for cmb in combin:
    q = deque()
    visited = [[0]*N for _ in range(N)]
    for i in cmb:
        q.append(i)
    for j in q:
        visited[j[0]][j[1]] = 1
    # print(q)
    # print(house)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] += visited[x][y] + 1
                    q.append([nx,ny])
    temp = 0
    for x,y in house:
        temp += visited[x][y]-1
    result = min(temp,result)
    # print(visited)
print(result)