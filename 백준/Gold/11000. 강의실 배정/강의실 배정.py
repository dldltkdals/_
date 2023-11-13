N = int(input())
import heapq
TimeTable = [list(map(int,input().split(" "))) for _ in range(N)]
TimeTable.sort(key = lambda x: (x[0],x[1]))


    
heap = [TimeTable[0][1]]

for i in range(1,N):
    if heap[0] <= TimeTable[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,TimeTable[i][1])
print(len(heap))