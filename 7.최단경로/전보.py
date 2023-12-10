import sys
import heapq
sys.stdin = open("7.최단경로/input.txt")

INF = int(1e9)
node, edge, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    fromNode, toNode, weight = map(int, sys.stdin.readline().split())
    graph[fromNode].append((toNode, weight))


distance = [INF]* (node+1)
cnt = 0
def dijkstrat(start):
    global cnt
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start)) # weight, node
    
    while q:
        dis, curr = heapq.heappop(q)
        if distance[curr] < dis:
            continue
        for data in graph[curr]:
            cost = dis + data[1]
            if cost < distance[data[0]]:
                cnt = cnt +1
                distance[data[0]] = cost 
                heapq.heappush(q, (cost, data[0]))
dijkstrat(start)
max_dis = 0
for dis in distance:
    if dis != INF:
        if max_dis < dis:
            max_dis = dis
print(cnt, max_dis)
        
    


