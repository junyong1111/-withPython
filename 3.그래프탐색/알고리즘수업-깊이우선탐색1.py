import sys
sys.setrecursionlimit(10 ** 6) 
#-- 메모리 초과가 날 수 있으므로 최대 깊이는 최대 노드 수를 넘을 수 없으니 최대 노드 수로 설정하자 불안하면 +1
# sys.stdin = open("3.그래프탐색/input.txt")

node, edge, startnode = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(node+1)] 

for i in range(edge):
    fromnode, tonode = map(int, sys.stdin.readline().split())
    graph[fromnode].append(tonode)
    graph[tonode].append(fromnode)
for i in range(1, node+1):
    graph[i] = sorted(graph[i])
visit = [0] * (node+1)

cnt = 0
def dfs(node):
    global cnt
    cnt = cnt +1
    visit[node] = cnt
    for vertext in graph[node]:
        if visit[vertext] == 0 :
            dfs(vertext)
dfs(startnode)
        
for i in range(1, node+1):
    print(visit[i])