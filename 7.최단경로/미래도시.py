import sys
sys.stdin = open("7.최단경로/input.txt")

INF = int(1e9)
node, edge = map(int, sys.stdin.readline().split())
graph = [[INF] * (node+1) for _ in range(node+1)]

def my_print(node):
    for i in range(1, node+1):
        for j in range(1, node+1):
            print(graph[i][j], end=" ")
        print()

for i in range(1, node+1):
    for j in range(1, node+1):
        if i == j:
            graph[i][j] = 0

weight = 1
for _ in range(edge):
    fromNode, toNode = map(int, sys.stdin.readline().split())
    graph[fromNode][toNode] = weight   

for k in range(1, node+1):
    for f in range(1, node+1):
        for t in range(1, node+1):
            graph[f][t] = min(graph[f][t],
                              graph[f][k]+graph[k][t])
            
datelocation, meetinglocation = map(int, sys.stdin.readline().split())
answer = 1
answer += graph[1][datelocation]
answer += graph[datelocation][meetinglocation]

if answer >= INF:
    print(-1)
else:
    print(answer)


