import sys
import heapq
sys.setrecursionlimit(10**6)
sys.stdin = open("7.최단경로/input.txt")
INF = int(1e9)
node, edge = map(int, sys.stdin.readline().split())
s_node = int(sys.stdin.readline())

# print(node, edge, s_node)
graph = [[] for _ in range(node+1)]
distance = [INF] * (node+1)

for i in range(edge):
    fromNode, toNode, weight = map(int, sys.stdin.readline().split())
    graph[fromNode].append((toNode, weight))

def dijkstra(s_node):
    queue = []
    heapq.heappush(queue, (0, s_node))
    distance[s_node] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))
            
        
dijkstra(s_node)

for i in range(1, node+1):
    if distance[i] == INF:
        print("IMPOSSIBLE")
    else:
        print(distance[i])
    
    

# print(queue)

# toNode, Weight



