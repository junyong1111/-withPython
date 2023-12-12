import sys
from collections import deque
# sys.stdin = open("3.그래프탐색/input.txt")

def myprint(graph, n, m):
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end=' ')
        print()
     
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
M, N = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
distance = [[0 for _ in range(M)] for _ in range(N)]
tomatos = []
flag = False

q = deque()

for i in range(N):
    data = sys.stdin.readline().split()
    for j in range(M):
        graph[i][j] = int(data[j])
        if graph[i][j] == 1:
            q.append((j, i))
        else:
            flag = True

def bfs(q):
    while q:
        x, y = q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if nx>=0 and ny>=0 and nx<M and ny <N and graph[ny][nx] == 0 and distance[ny][nx] == 0:
                graph[ny][nx] = 1
                distance[ny][nx] = distance[y][x]+1
                q.append((nx, ny))
    
def checkTomato(graph, n, m):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

if flag == False:
    print(0)
else:
    bfs(q)
    if checkTomato(graph, N, M) == False:
        print(-1)
    else:
        print(max(map(max, distance)))
        # myprint(distance, N, M)
        
        