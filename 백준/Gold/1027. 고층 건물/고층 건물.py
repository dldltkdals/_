N = int(input())

heights = list(map(int,input().split(" ")))
bulidings = [(i,h) for i,h in enumerate(heights)]
result = 0
# print(bulidings)
def slope(c1,c2):
    x1,y1 = c1
    x2,y2 = c2
    return (y1-y2)/(x1-x2)
    
for temp in range(len(bulidings)):
    Lcount = 0
    Rcount = 0
    left_max = float('inf')
    right_max = float('-inf')
    for left in range(temp-1,-1,-1):
        temp_slope = slope(bulidings[temp],bulidings[left])
        if temp_slope < left_max:
            left_max = temp_slope
            Lcount += 1


   
    for right in range(temp+1,len(bulidings)):
        temp_slope = slope(bulidings[temp],bulidings[right])
        if temp_slope > right_max:
            right_max = temp_slope
            Rcount += 1

    result = max(result,Rcount+Lcount)
    # print(f"result: {result}, bulidings: {bulidings[temp]}, left {Lcount} , right: {Rcount}")
    
# print()
print(result)