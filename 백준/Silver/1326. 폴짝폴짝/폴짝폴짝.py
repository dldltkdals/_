from collections import deque

N = int(input())
stones = list(map(int,input().split()))

start,destinetion = list(map(int,input().split()))


q = deque([start-1])
bound = N//min(stones)
visited = [0]*(N)
visited[start-1] = 1
while q:
    temp = q.popleft()

    for i in range(1,N):
        next = i*stones[temp] + temp
        if 0 <= next < N:
            if not visited[next]:
                visited[next] = (visited[temp] +1)
                q.append(next)
                if next == destinetion-1:
                    # print(visited)
                    print(visited[next]-1)
                    exit(0)
        else:
            break
    for i in range(1,N):
        next = -1*i*stones[temp] + temp
        if 0 <= next < N:
            if not visited[next]:
                visited[next] = (visited[temp] +1)
                q.append(next)
                if next == destinetion-1:
                    # print(visited)
                    print(visited[next]-1)
                    exit(0)
        else:
            break
# print(visited)
print(visited[destinetion-1]-1)