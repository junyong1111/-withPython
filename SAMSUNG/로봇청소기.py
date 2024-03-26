import sys
from collections import deque
# sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline
 
#-- 북 동 남 서
dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
room = [[0 for _ in range(M)] for _ in range(N)]
robot = list(map(int, input().split())) #-- Y, X, D

for i in range(N):
    data = input().split()
    for j in range(M):
        room[i][j] = int(data[j])

def myprint():
    for i in range(N):
        for j in range(M):
            print(room[i][j], end=" ")
        print()

#-- init()
# myprint()

answer = 0
def CleanRoom(x, y):
    global answer
    if room[y][x] == 0:
        answer+=1
        room[y][x] = -1

def isMove(nx, ny):
    if nx < 0 or nx >= M:
        return False
    if ny < 0 or ny >= N:
        return False
    return True
    
def checkRoom(x, y):
    #-- 4방향 체크 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #-- 청소가 가능한지 확인하고 가능하다면 True
        if isMove(nx, ny) and room[ny][nx] == 0:
            return True
    
    return False
            
        
def rotate():    
    dir = robot[2]
    #-- 북 -> 서
    if dir == 0: 
        dir = 3
    #-- 동 -> 북    
    elif dir == 1:
        dir = 0
    #-- 남 -> 동
    elif dir == 2:
        dir = 1
    #-- 서 ->남
    elif dir == 3:
        dir = 2
    robot[2] = dir
        
        
        
def move(x, y):
    dir = robot[2]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if room[ny][nx] == 0:
        robot[0],robot[1] = ny, nx
        return True
    return False
    
    
def moveBack(x, y):
    dir = robot[2]
    #-- 북 동 남 서
    if dir == 0:
        nx = x
        ny = y+1
    elif dir == 1:
        nx = x-1
        ny = y
    elif dir ==2:
        nx = x
        ny = y-1
    elif dir == 3:
        nx = x+1
        ny = y
    
    if isMove(nx, ny) and room[ny][nx] != 1:
        robot[0], robot[1] = ny, nx
        return True
    return False
    
            
    
while True:
    y, x, _ = robot
    #-- step1. 해당 자리가 청소되어 있는지 확인하고 청소되어지 않다면 정답 +1
    CleanRoom(x, y)
    
    #-- step2. 주변 청소 확인
    #-- step 2-1 빈칸이 존재하는경우
    if checkRoom(x, y) == True:
        for _ in range(4):
            #-- 반시계 90도 회전
            rotate()
            if move(x, y):
                break
    #-- step 2-2 빈칸이 없는 경우
    else:  
        if moveBack(x, y) == False:
            break
print(answer)