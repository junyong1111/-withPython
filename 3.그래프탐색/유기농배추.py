import sys
from collections import deque
# sys.stdin = open('3.그래프탐색/input.txt')

testCase = int(sys.stdin.readline())
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = []

while testCase:
    testCase-=1
    x, y, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(x)] for _ in range(y)]
    
    for _ in range(k):
        kx, ky = map(int, sys.stdin.readline().split())
        graph[ky][kx] = 1
    
    def bfs(q):
        while q:
            ox, oy = q.popleft()
            for move in moves:
                nx = ox + move[0]
                ny = oy + move[1]
                if nx>=0 and ny>=0 and nx<x and ny<y and graph[ny][nx] ==1:
                    graph[ny][nx] = 0
                    q.append((nx, ny))
    cnt = 0 
    for i in range(y):
        for j in range(x):
            if graph[i][j] == 1:
                q = deque()
                q.append((j, i))
                graph[i][j] = 0
                bfs(q)
                cnt +=1 
    
    answer.append(cnt)
for ans in answer:
    print(ans)