import sys
from collections import deque
# sys.stdin = open('3.그래프탐색/input.txt')

steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().split()
    for j in range(m):
        graph[i][j] = int(line[0][j])

def bfs(q):    
    while q:
        x, y = q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                distance[ny][nx] = distance[y][x]+1
                q.append((nx, ny))
q = deque()
q.append((0, 0))
distance[0][0] = 1
bfs(q)
print(distance[n-1][m-1])