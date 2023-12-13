import sys
from collections import deque
sys.stdin = open("3.그래프탐색/input.txt")

steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N,M = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(M+1)] for _ in range(N+1)]
distance = [[[0]*2 for _ in range(M+1)]for _ in range(N+1)]

for i in range(1, N+1):
    data = sys.stdin.readline().split()
    for j in range(1, M+1):
        board[i][j] = int(data[0][j-1])

def myprint(string):
    if string == "dis":
        for h in range(2):
            for i in range(1, N+1):
                for j in range(1, M+1):
                    print(distance[i][j][h], end =' ')
                print()
            print()
    else:
        for i in range(1, N+1):
            for j in range(1, M+1):
                print(board[i][j], end=' ')
            print()

myprint('dis')
def bfs():
    q = deque()
    q.append((1, 1, 0))
    distance[1][1][0] = 1
    
    while q:
        x, y, crashed = q.popleft()
        if x == M and y == N:
            return distance[y][x][crashed]
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 1<=nx<=M and 1<=ny<=N and distance[ny][nx][crashed] == 0:
                if board[ny][nx] == 0: #-- 갈 수 있는 곳이면 감
                    distance[ny][nx][crashed] = distance[y][x][crashed]+1
                    q.append((nx, ny, crashed))
                else:#-- 벽인 경우 벽을 1회 부수거나 부수지 않거나 택 1
                    if crashed == 1: #--이미 벽이 부서줘 있다면 그냥 지나감
                        continue
                    else: #--부술 수 있다면 임의로 부숴서 최단거리 갱신
                        distance[ny][nx][crashed+1] = distance[y][x][crashed]+1
                        q.append((nx, ny, crashed+1))
    return -1            
                        
ans = bfs()
print(ans)