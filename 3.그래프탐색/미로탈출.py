'''
s = 1,1 
f = n,m
괴물 있음 = 0
괴물 없음 =  1
1번에 1칸 이동 가능 
'''

import sys
from collections import deque
import pprint
sys.stdin = open('3.그래프탐색/input.txt')

n,m = map(int, sys.stdin.readline().split())
graph = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    data = sys.stdin.readline()
    for j in range(m):
        graph[i][j+1] = int(data[j])

steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]        


def bfs():
    queue = deque([(1, 1)]) #-- x, y
    distance =[[0 for j in range(m+1)] for i in range(n+1)]
    distance[1][1] = 1
    
    while(queue):
        x, y = queue.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if (nx >= 1 and nx <= m) and (ny > 0 and ny <= n) and(distance[ny][nx] == 0) and (graph[ny][nx] == 1):
                distance[ny][nx] = distance[y][x] + 1
                queue.append((nx, ny))
                
    if distance[n][m] != 0:
        return distance[n][m]
    else:
        return -1

result = bfs()
print(result)