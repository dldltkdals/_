from collections import deque

N = int(input())

temp = [input().split() for _ in range(N)]
tPosition = list()
sPosition = list()
for i in range(N):
    for j in range(N):
        if temp[i][j] == "T":
            tPosition.append([i,j])
        elif temp[i][j] == "S":
            sPosition.append([i,j])

def check(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in tPosition:# 선생님의 위치에서
        for k in range(4): # 상/하/좌/우 탐색
            nx, ny = t

            while 0 <= nx < N and 0 <= ny < N:
                if temp[nx][ny] == "O":
                    break

                # 학생이 보이면 실패
                if temp[nx][ny] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]

    # 모두 통과하면 학생이 안보이는 것으로 성공
    return True

        


def setObject(count):
    if count == 3:
        for x,y in tPosition:
            if not check(x,y):
                return
        print("YES")
        exit()
    for i in range(N):
        for j in range(N):
            if temp[i][j] == "X":
                temp[i][j] = "O"
                setObject(count+1)
                temp[i][j] = "X"
setObject(0)
print("NO")



            
        