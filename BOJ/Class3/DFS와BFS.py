import sys
from collections import deque
sys.setrecursionlimit(10000)
# sys.stdin = open("BOJ/Class3/input.txt")

node, edge, start_node = map(int, sys.stdin.readline().split())
# print(node, edge, start_node)
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    a, b= map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, node+1):
    graph[i].sort()

visit = [False] * (node+1)
def dfs(node):
    visit[node] = True
    print(node, end=" ")
    for i in range(len(graph[node])):
        if visit[graph[node][i]] == False:
            dfs(graph[node][i])
 

visit_bfs = [False] * (node+1)
queue = deque()
def bfs(node):
    visit_bfs[node] = True
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(len(graph[node])):
            if visit_bfs[graph[node][i]] == False:
                visit_bfs[graph[node][i]] = True
                queue.append(graph[node][i])
     
dfs(start_node)
print()
bfs(start_node)
print()
