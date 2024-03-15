import sys
# sys.stdin = open("BOJ/Class3/input.txt")

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]

#-- 그래프 연결
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

#-- DFS 선언
visit = [False] * (V+1)
def dfs(start):
    stack = []
    stack.append(start)
    visit[start] = True
    while stack:
        node = stack.pop()
        #-- 해당 노드에 연결된 모든 엣지들 탐색
        for n in graph[node]:
            if visit[n] == False:
                visit[n] = True
                stack.append(n)
answer = 0             
for node in range(1, V+1):
    if visit[node] == False:
        dfs(node)
        answer +=1
print(answer)
