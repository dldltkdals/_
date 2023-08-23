'''
사탕게임
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
가장 처음에 N×N크기에 사탕을 채워 놓는다.사탕의 색은 모두 같지 않을 수도 있다. 
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음
그 사탕을 모두 먹는다. 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 
사탕의 최대 개수를 구하는 프로그램을 작성하시오.

반례
5 
CPZCC
ZYCPZ
CYYPZ
ZPZCC
CCPYY
답3, 출력 2
'''
N = int(input())
candy_board = [list(input()) for _ in range(N)]
#행과 열의 가장 긴 사탕 개수를 반환
def count_candy(candy_board):
    max_count = 1
    for i in range(N):
        curr = candy_board[i][0]
        count = 1
        for j in range(1,N):
            temp = candy_board[i][j]
            if temp == curr:
                count += 1
            else: 
                max_count = max(count, max_count)
                count = 1
            curr = temp
        max_count = max(count, max_count)
    for i in range(N):
        curr = candy_board[0][i]
        count = 1
        for j in range(1,N):
            temp = candy_board[j][i]
            if temp == curr:
                count += 1
            else: 
                max_count = max(count, max_count)
                count = 1
            curr = temp
        max_count = max(count, max_count)
    return max_count
#사탕 두개를 교환
#1-1) 같은 행끼리 교환
max_count = 1
for i in range(N):
    for j in range(1,N):
        candy_board[i][j-1],candy_board[i][j] = candy_board[i][j],candy_board[i][j-1]
        max_count = max(count_candy(candy_board),max_count)
        candy_board[i][j-1],candy_board[i][j] = candy_board[i][j],candy_board[i][j-1]

# 1-2) 같은 열끼리 교환
for i in range(1,N):
    for j in range(N):
        candy_board[i-1][j],candy_board[i][j] = candy_board[i][j],candy_board[i-1][j]
        max_count = max(count_candy(candy_board),max_count)
        candy_board[i-1][j],candy_board[i][j] = candy_board[i][j],candy_board[i-1][j]


print(max_count)