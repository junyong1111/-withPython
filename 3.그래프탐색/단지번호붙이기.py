import sys
from collections import deque

# sys.stdin = open("3.그래프탐색/input.txt")
n = int(sys.stdin.readline())

graph = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    line = sys.stdin.readline().split()
    for j in range(n):
        graph[i][j] = int(line[0][j])

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs(q):
    
    cnt = 1
    while q:
        ox, oy = q.popleft()
        for move in moves:
            nx = ox + move[0]
            ny = oy + move[1]
            if nx >= 0 and ny >=0 and nx<n and ny<n and graph[ny][nx] !=0:
                cnt = cnt+1
                graph[ny][nx] = 0
                q.append((nx, ny))
    return cnt    
        
answer = []
ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            q = deque()
            q.append((j,i))
            graph[i][j] = 0
            answer.append(bfs(q))
            ans +=1
    
print(len(answer))
answer.sort()
for ans in answer:
    print(ans) 