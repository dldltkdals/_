'''

'''
import sys
from collections import deque
iString = sys.stdin.readline().rstrip().strip(" ")
N = int(sys.stdin.readline().rstrip().strip(" "))
LeftStack = deque(list(iString))
RightQueue = deque()
for _ in range(N):
    command = sys.stdin.readline().rstrip().strip(" ")
    if command == "L":#커서 왼쪽이동
        if LeftStack:# 왼쪽 커서가 비어있지 않다면
            RightQueue.appendleft(LeftStack.pop())
    elif command == "D": #커서 오른쪽 이동
        if RightQueue:# 오른쪽 커서가 비어있지 않다면
        
            LeftStack.append(RightQueue.popleft())
    elif command == 'B':
        if LeftStack:# 왼쪽 커서가 비어있지 않다면
            LeftStack.pop()
    else:
        LeftStack.append(command[-1])
print("".join(list(LeftStack+RightQueue)))