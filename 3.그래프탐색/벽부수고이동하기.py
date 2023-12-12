import sys
from collections import deque
# sys.stdin = open("3.그래프탐색/input.txt")
INF = int(1e9)
MAX_SIZE = 1001
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, sys.stdin.readline().split())
MAP = [[0 for _ in range(M+1)] for _ in range(N+1)]
wall = []

for i in range(1, N+1):
    data = sys.stdin.readline().split()
    for j in range(1, M+1):
        MAP[i][j] = int(data[0][j-1])
        if MAP[i][j] == 1:
            wall.append((j, i))

def myprint():
    for i in range(1, N+1):
        for j in range(1, M+1):
            print(MAP[i][j], end=' ')   
        print()

distance = arr = [[[0]*2 for _ in range(M+1)] for _ in range(N+1)]

def bfs(myMap):
    flag = False
    distance[1][1][0] = 1
    q = deque()
    q.append((1, 1, 0))
    while q:
        if flag == True:
            break
        x, y, crashed= q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0<nx<=M and 0<ny<=M:
                if myMap[ny][nx] == 0 and distance[ny][nx] == 0:
                    distance[ny][nx][crashed] = distance[y][x][crashed] +1
                elif myMap[ny][nx] == 1 and crashed == 0:
                    distance[ny][nx][crashed+1]
                    
                    
                
                
                
                
                
                if ny == N and nx == M:
                    flag = True
                    break
                q.append((nx, ny))
    if distance[N][M] == 0:
        return INF
    return distance[N][M]

min_dis = bfs(MAP)

for w in wall:
    x, y = w
    MAP[y][x] = 0
    min_dis = min(min_dis, bfs(MAP))
    MAP[y][x] = 1

if min_dis == INF:
    print(-1)
else: 
    print(min_dis)