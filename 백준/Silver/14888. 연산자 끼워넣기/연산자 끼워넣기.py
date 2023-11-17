N = int(input())
numbers = list(map(int,input().split(" ")))
operation = list(map(int,input().split(" ")))
idx = 0
minValue, maxValue = float("inf"),float("-inf")

def backTracking(curr,temp_idx,Opt):
    global minValue, maxValue
    if temp_idx >= len(numbers):
        minValue = min(minValue,curr)
        maxValue = max(maxValue,curr)
        return
    result = curr
    for i in range(len(Opt)):
        if Opt[i]==0:
            continue
        if i == 0:
         
            Opt[i] -= 1
            backTracking(result+numbers[temp_idx],temp_idx+1,Opt)
            Opt[i] += 1
            
        elif i == 1:
         
            Opt[i] -= 1
            backTracking(result-numbers[temp_idx],temp_idx+1,Opt)
            Opt[i] += 1
         

        elif i == 2:
            
            Opt[i] -= 1
            backTracking(result*numbers[temp_idx],temp_idx+1,Opt)
            Opt[i] += 1
        else:
            Opt[i] -= 1
            if result < 0:
                backTracking(abs(result)//numbers[temp_idx]*-1,temp_idx+1,Opt)
            else:
                backTracking(result//numbers[temp_idx],temp_idx+1,Opt)
            Opt[i] += 1
            
            
            
backTracking(numbers[0],1,operation)
print(maxValue)
print(minValue)
