'''
문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
'''
N, M = [*map(int,input().split())]
Map = [ list(input().split()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
distance = [[-1]*M for _ in range(N)]
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
for i in range(N):
    for j in range(M):
        if Map[i][j] == '2':
            q.append([i,j])
            visited[i][j] = 1
            distance[i][j] = 0
        elif Map[i][j] == '0':
            distance[i][j] = 0

        
            

while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y + dy[i]
        if 0<= nx < N and 0 <= ny <M:
            if not visited[nx][ny] and Map[nx][ny] == '1':
                q.append([nx,ny])
                visited[nx][ny] = 1 + visited[x][y]
                distance[nx][ny] += visited[nx][ny]
for i in range(N):
    print(*distance[i])



