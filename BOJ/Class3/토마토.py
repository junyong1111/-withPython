import sys
from collections import deque
# sys.stdin = open("BOJ/Class3/input.txt")

M,N = map(int, sys.stdin.readline().split())
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
tomatos = deque()
grid = [[0 for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

zero = False
for i in range(N):
    data = sys.stdin.readline().split()
    for j in range(M):
        grid[i][j] = int(data[j])
        if grid[i][j] == 1:
            tomatos.append((j, i))
            #-- tomato가 있는 위치만 미리 선택
        if grid[i][j] == 0:
            zero = True

if zero == False:
    #-- 이미 모두 익어 있는 경우 
    print(0)
    sys.exit(0)
    

def dfs(x, y):
    visit[y][x] = True
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == 0 and visit[ny][nx] == False:
            grid[ny][nx] = 1
            tomatos.append((nx, ny))

def isPossible():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                return False
    return True
           
day = 0
while True:    
    size = len(tomatos)
    for i in range(size):
        x, y = tomatos.popleft()
        if visit[y][x] == False:
            dfs(x, y)
    if len(tomatos) == 0:
        break    
    day +=1

if isPossible():    
    print(day)
else:
    print(-1)    
