from collections import deque


N = int(input())
stack = deque()
result = 0
for _ in range(N):
    position, height = list(map(int,input().split(" ")))
    
    if not stack:
        stack.append(height)
    else:
        if stack[-1] > height:
            while stack and stack[-1] > height:
                stack.pop()
                result += 1
            if stack:
                if stack[-1] == height:
                    continue
            stack.append(height)
        elif stack[-1] < height:
            stack.append(height) 
if stack:
    for s in stack:
        if s:
            result += 1              


print(result)