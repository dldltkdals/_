'''
N번째로 큰수
5 7 9 12 15
6 8 11 13 19
10 16 21 26 31
14 25 28 35 48
20 32 41 49 52
'''
from queue import PriorityQueue
import heapq
N = int(input())

# graph = [list(map(int,input().split())) for _ in range(N)]
# for i in range(N):
#     graph[i].sort()
# que = PriorityQueue()
heap = []
for row in range(N):
    for col in map(int,input().split()):
        heapq.heappush(heap,col)
        if len(heap) > N:
            heapq.heappop(heap)
        # que.put(col)
        # if que.qsize() > N:
            # que.get()
        
       
print(heapq.heappop(heap))
# print(que.get())

