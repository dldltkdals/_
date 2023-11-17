N, M  = list(map(int,input().split(" ")))
woods = list(map(int,input().split(" ")))

minH = 0
maxH = max(woods)

def binary(s,e):
    tempH = (s+e)//2
    total_wood = 0

    if s>e:
        return e 
    for i in range(len(woods)):
        if woods[i]>tempH:
            total_wood += (woods[i]-tempH)
    
    if total_wood >= M:
        return binary(tempH+1,e)
    else:
        return binary(s,tempH-1)
 
print(binary(minH,maxH))