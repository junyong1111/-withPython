import sys
from collections import deque
# sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline
N, M, X, Y, K = map(int, input().split())
start = deque()
start.append([Y, X])
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
FRONT = 4
BACK = 5
# print(N, M, X, Y, order)

grid = [[0 for _ in range(M)] for _ in range(N)]

dice = [0, 0, 0, 0, 0, 0] #-- U D R L F B


for i in range(N):
    data = input().split()
    for j in range(M):
        grid[i][j] = int(data[j])

# def myprint():
#     for i in range(N):
#         for j in range(M):
#             print(grid[i][j], end=" ")
#         print()
#     print(start)
# myprint()

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
# #-- X, 동, 서, 북, 남
orders = list(map(int, input().split()))

def isPossible(nx, ny):
    if nx < 0 or nx >= M:
        return False
    if ny < 0 or ny >= N:
        return False
    return True

def moveDice(dir):
    tempUp = dice[UP]
    tempDw = dice[DOWN]
    tempLeft = dice[LEFT]
    tempRight = dice[RIGHT]
    tempFront = dice[FRONT]
    tempBack = dice[BACK]
    #-- 동
    if dir == 1:
        dice[UP] = tempLeft
        dice[DOWN] = tempRight
        dice[LEFT] = tempDw
        dice[RIGHT] = tempUp
    #-- 서
    elif dir == 2:
        dice[UP] = tempRight
        dice[DOWN] = tempLeft
        dice[LEFT] = tempUp
        dice[RIGHT] = tempDw
    #-- 북
    elif dir == 3:
        dice[UP] = tempFront
        dice[DOWN] = tempBack
        dice[FRONT] = tempDw
        dice[BACK] = tempUp
    #-- 남
    elif dir == 4:
        dice[UP] = tempBack
        dice[DOWN] = tempFront
        dice[FRONT] = tempUp
        dice[BACK] = tempDw
        
for order in orders:
    #-- step1. 주사위 위치에서 명령어 방향으로 이동
    if len(start) != 0:
        x, y = start.popleft()
    nx = x + dx[order]
    ny = y + dy[order]
    
    #-- step.2 범위 밖이라면 그냥 무시
    if isPossible(nx, ny) == False:
        start.append([x, y])
        continue
    
    #-- step.3 이동 
    start.append([nx, ny])
    moveDice(order)
    #-- step3-1 만약 바닥이 0이라면 주사위 바닥에 있는 값을 맵 바닥으로
    if grid[ny][nx] == 0:
        grid[ny][nx] = dice[DOWN]
    #-- step3-2 그게 아니라면 맵 바닥에 있는 값을 -> 주사위 바닥으로 옮기고 맵은 0으로
    else:
        dice[DOWN] = grid[ny][nx]
        grid[ny][nx] = 0
    print(dice[UP])