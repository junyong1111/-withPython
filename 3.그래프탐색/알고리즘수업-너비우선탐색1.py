
import sys
from collections import deque
sys.setrecursionlimit(100001)
# sys.stdin = open("3.그래프탐색/input.txt")

node, edge, s_node = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for i in range(edge):
    fromNode, toNode = map(int, sys.stdin.readline().split())
    graph[fromNode].append(toNode)
    graph[toNode].append(fromNode)

for i in range(1, node+1):
    graph[i] = sorted(graph[i])

queue = deque()
visit = [0] * (node+1)
queue.append(s_node)
cnt = 1
visit[s_node] = cnt

def bfs():
    global cnt
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visit[n] == 0: 
                cnt = cnt+1
                visit[n] = cnt
                queue.append(n)
bfs()
for i in range(1, node+1):
    print(visit[i])