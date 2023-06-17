from collections import deque
N,M = list(map(int,input().split()))
nums = sorted(list(map(int,input().split())))
check = set()
result = deque()
def recur(nums,check):

    if len(result) == M:
        print(*result)
        return

    for num in nums:
        if num in check:
            continue
        result.append(num)
        check.add(num)
        recur(nums,check)
        result.pop()
        check.remove(num)

recur(nums,check)
# 1 7 8 9
