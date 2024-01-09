import sys
from collections import deque
# sys.stdin = open("BOJ/Class3/input.txt")

def myprint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

distance = [[-1 for _ in range(m)] for _ in range(n)]
queue = deque()
def bfs(start):
    x, y  = start
    queue.append((x, y))
    distance[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0<=nx<m and 0<=ny<n and distance[ny][nx]==-1 and grid[ny][nx] == 1:
                distance[ny][nx] = distance[y][x] + 1
                queue.append((nx, ny))
    return distance
        
    
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            bfs((j, i))
  
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0: #-- 기존에 갈 수 없었던 땅은 0으로 표시
            distance[i][j] = 0   
            
myprint(distance, n, m)