import sys
from collections import deque
sys.setrecursionlimit(1001)
# sys.stdin = open('3.그래프탐색/input.txt')

node, edge, s_node = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for i in range(edge):
    fromNode, toNode = map(int, sys.stdin.readline().split())
    graph[fromNode].append(toNode)
    graph[toNode].append(fromNode)

for i in range(1, node+1):
    graph[i] = sorted(graph[i])

visit = [0] * (node+1)
visit[s_node] = 1

def dfs(node):
    print(node, end = " ")
    for n in graph[node]:
        if visit[n] == 0:
            visit[n] = 1
            dfs(n)
dfs(s_node)
print()

visit = [0] * (node+1)
visit[s_node] = 1
queue =deque()
queue.append(s_node)

def bfs():
    while queue:
        data = queue.popleft()
        print(data, end =" ")
        for node in graph[data]:
            if visit[node] == 0:
                visit[node] = 1
                queue.append(node)
bfs()
print()