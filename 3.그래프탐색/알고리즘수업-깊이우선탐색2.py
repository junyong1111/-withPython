import sys
sys.setrecursionlimit(100001)
# sys.stdin = open("3.그래프탐색/input.txt")

nodes, edges, startnode = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(nodes+1)]
visit = [0] * (nodes+1)

for i in range(edges):
    _from, _to = map(int, sys.stdin.readline().split())
    graph[_from].append(_to)
    graph[_to].append(_from)

for i in range(nodes+1):
    graph[i] = sorted(graph[i], reverse=True)
    
cnt = 0
def dfs(node):
    global cnt
    cnt = cnt +1
    visit[node] = cnt
    
    for n in graph[node]:
        if visit[n] == 0:
            dfs(n)
dfs(startnode)
for i in range(1, nodes+1):
    print(visit[i])