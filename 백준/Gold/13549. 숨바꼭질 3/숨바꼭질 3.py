'''
풀이시작: 14:25
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''
from collections import deque
#해당 좌표에 몇초만에 도착했는지 체크하는 배열: i 위치에 visited[i] 초에 최초 도착했다는 의미
visited = [-1]*100001 # 0<=N<=100000
N,K = list(map(int,input().split(" ")))
# 순간이동의 좌표를 체크하는 함수
def teleportation(x:int,q):
    second = visited[x]
    if x == 0:
        return
    while x <= 100000:
        if visited[x] == -1:
            visited[x] = second
            q.append(x)
        x = 2*x
#초기화
visited[N] = 0 #현재위치는 0초로 초기화
q = deque([N])
teleportation(N,q)
# print(visited[:21],q)

while q:
    x = q.popleft()
    for i in [-1,1]:
        nx = x+i
        if 0 <= nx <= 100000:
            if visited[nx] == -1:
                visited[nx] = visited[x]+1
                q.append(nx)
               
                teleportation(nx,q)
    if nx == K:
        break
print(visited[K])
