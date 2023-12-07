import sys
sys.stdin = open("7.최단경로/input.txt")
INF = int(1e9)

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[INF]*(node+1) for _ in range(node+1)]

for i in range(1, node+1):
    for j in range(1, node+1):
        if i == j:
            graph[i][j] = 0

for i in range(edge):
    fromNode, toNode, weight = map(int, sys.stdin.readline().split())
    graph[fromNode][toNode] = weight


def myprint(node):
    for i in range(1, node+1):
        for j in range(1, node+1):
            print(graph[i][j], end=" ")
        print()

for k in range(1, node+1):
    for fromNode in range(1, node+1):
        for toNode in range(1, node+1):
            graph[fromNode][toNode] = min(graph[fromNode][toNode], 
                                          graph[fromNode][k] + graph[k][toNode])
myprint(node)

