S = input()
P = input()
i = 0
count = 0
temp = P[i]
while i < len(P):
    # print(f"temp: {temp},i: {i}, count: {count}")
    if temp in S:
        i += 1
        if i == len(P):
            count += 1
            break
        temp += P[i]
        
    else:
        count += 1
        temp = P[i]
print(count)
  
