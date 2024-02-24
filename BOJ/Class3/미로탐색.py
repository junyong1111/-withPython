import sys
from collections import deque

# sys.stdin = open("BOJ/Class3/input.txt")

N, M = map(int ,sys.stdin.readline().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):
    data = sys.stdin.readline()
    for j in range(M):
        graph[i][j] = int(data[j])


queue = deque()
queue.append((0, 0))
distance = [[0 for _ in range(M)] for _ in range(N)]
distance[0][0] = 1
while queue:
    x, y = queue.popleft()
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if (0 <= nx <M and 0 <=ny < N and distance[ny][nx] == 0 and graph[ny][nx] == 1):
            #-- index 범위안에 있고, 방문한적이 없으며 이동할 수 있는 경우
            distance[ny][nx] = distance[y][x] + 1
            queue.append((nx, ny))
            

print(distance[N-1][M-1])