import sys
from collections import deque
# sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline

N = int(input())
K = int(input())

grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
grid[1][1] = 1

for _ in range(K):
    y, x = map(int, input().split())
    grid[y][x] = -1 #-- 사과 

moves = []
L = int(input())
for _ in range(L):
    t, dir = input().split()
    moves.append([int(t), dir])
   
moves = deque(moves) 
#-- init 

time = 0
t, direction = moves.popleft()

#-- R, D, L, W
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir = 0

snake = deque()
snake.append([1, 1])

while True:
    # break
    time +=1
    
    #-- 몸길이 증가 -> 머리를 다음칸
    nx = snake[-1][0]+ dx[dir]
    ny = snake[-1][1] + dy[dir]
    
    #-- 벽 또는 자기 자신이 아니면 게임 진행
    if 1 <= nx <= N and 1 <= ny <= N and grid[ny][nx] != 1:
        #-- 사과가 없다면 꼬리 전진 
        if grid[ny][nx] != -1:
            tx, ty = snake.popleft()
            grid[ty][tx] = 0
        
        grid[ny][nx] = 1
        snake.append([nx, ny])
    else:
        break
    #-- 정해진 시간이 지나면 방향 바꾸기
    if t == time:
        #-- L : 현재 진행에서 왼쪽으로 90도
        if direction == "L":
            dir = (dir-1)%4
        #-- D : 현재 진행에서 오른쪽으로 90도 방향 회전
        else:
            dir = (dir+1)%4
        if len(moves) != 0:
            t, direction = moves.popleft()
        
print(time)