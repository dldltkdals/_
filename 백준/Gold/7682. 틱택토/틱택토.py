'''
https://www.acmicpc.net/problem/7682
18:20

xox
oxo
xox

.xx
x.x
ooo
'''
import sys

ttt = True
#
def InvalidCheck(phase,ttt):

    invalid_check = 3*phase[1]

    if ttt[:3] == invalid_check:
        invalid_flag = True

    elif ttt[3:6] == invalid_check:
        invalid_flag = True

    elif ttt[6:] == invalid_check:
        invalid_flag = True
    
    elif ttt[0]+ttt[4]+ttt[8] == invalid_check:
        invalid_flag = True
    elif ttt[2]+ttt[4]+ttt[6] == invalid_check:
        invalid_flag = True
    
    elif ttt[0]+ttt[3]+ttt[6] == invalid_check:
        invalid_flag = True
    elif ttt[1]+ttt[4]+ttt[7] == invalid_check:
        invalid_flag = True
    elif ttt[2]+ttt[5]+ttt[8] == invalid_check:
        invalid_flag = True
    else:
        invalid_flag = False
    

    
    
    return invalid_flag
        
    
    

        
ttt = sys.stdin.readline().rstrip()

while ttt != "end":
    
    x_count = ttt.count("X")
    o_count = ttt.count("O")
    invalid_flag = True
    if x_count == o_count+1: #x가 이겼을 시나리오
        invalid_flag = InvalidCheck(("X","O"),ttt)
    elif x_count == o_count: #y가 이겼을 시나리오
        invalid_flag = InvalidCheck(("O","X"),ttt)
    
    if x_count + o_count < 9:
        if  not (InvalidCheck(("X","O"),ttt) or InvalidCheck(("O","X"),ttt)):
            invalid_flag = True
    
    
    
    
    if invalid_flag:
        print("invalid")
    else:
        print("valid")    
    ttt = sys.stdin.readline().rstrip()
    
        
    

 


    

    