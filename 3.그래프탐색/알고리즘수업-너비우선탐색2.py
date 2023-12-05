
import sys
from collections import deque
sys.setrecursionlimit(100001)
# sys.stdin = open("3.그래프탐색/input.txt")

node, edge, s_node = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    fromNode, toNode = map(int, sys.stdin.readline().split())
    graph[fromNode].append(toNode)
    graph[toNode].append(fromNode)

for i in range(1, node+1):
    graph[i] = sorted(graph[i], reverse = True)

visit = [0] * (node+1) 
queue = deque()

cnt = 1
visit[s_node] = cnt
queue.append(s_node)

def bfs():
    global cnt
    while queue:
        data = queue.popleft()
        for node in graph[data]:
            if visit[node] == 0:
                cnt = cnt+1
                visit[node] = cnt
                queue.append(node)

bfs()
for i in range(1, node+1):
    print(visit[i])
