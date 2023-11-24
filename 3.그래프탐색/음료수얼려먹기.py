'''
구멍 0
칸막이 1
상하좌우 이동 가능 
0으로 이루어진 아이스크림 몇 개?
dfs or bfs 노상관
'''

import sys
import pprint
sys.stdin = open('3.그래프탐색/input.txt')


steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]

n, m = map(int, sys.stdin.readline().split())
graph = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    data = sys.stdin.readline()
    for j in range(m):
        graph[i][j] = int(data[j])

answer= 0 

def dfs(y, x):
    graph[y][x] = 1
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if (nx >= 0 and nx < len(graph[0]) and (ny >=0 and ny <len(graph))):
            if(graph[ny][nx] == 0):
                graph[ny][nx] = 1
                dfs(ny ,nx)
                
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer+= 1
            dfs(i, j)
        # print(graph[i][j], end=' ')
        # 
print(answer)

