'''
https://www.acmicpc.net/problem/20006
시작시간 21:22

입력
플레이어수(p), 닉네임(n), 플레이어레벨(l), 방하나의 정원(m)
p, m

'''
from collections import deque
P,M = list(map(int,input().split(" ")))
#현재 개설된 방 목록
result = []
OpenedRooms = None
for _ in range(P):
    l,n = list(input().split(" "))
    l = int(l)
    #방을 새로 개설해야 되는지 확인하는 변수 (True=방개설해야됨)
    OpenFlag = True
    if not OpenedRooms:
        #만약 개설된 방이 없으면 방장의 레벨과 방장의 정보를 append
        OpenedRooms = deque([[l,[l,n]]])

    else:
        for i in range(len(OpenedRooms)):
            room = OpenedRooms[i]
            if len(room) < M+1:
                left_bound = room[0]-10
                right_bound = room[0]+10
                if left_bound <= l <= right_bound:
                    OpenedRooms[i].append([l,n])
                    OpenFlag = False 
                    break
        if OpenFlag:
            OpenedRooms.append([l,[l,n]])
         
        
for rooms in OpenedRooms:
    if len(rooms) < M+1:
        print("Waiting!")
    else:
        print("Started!")
        
    
    rooms = rooms[1:]
    rooms.sort(key=lambda x:(x[1],x[0]))
    for room in rooms:
        print(" ".join(map(str,room)))