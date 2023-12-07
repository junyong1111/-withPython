import sys
import heapq
# sys.stdin = open("input.txt")
INF = int(1e9)

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    fromNode, toNode, weight = map(int, sys.stdin.readline().split())
    graph[fromNode].append((toNode, weight))
    graph[toNode].append((fromNode, weight))

first_node, second_node = map(int, sys.stdin.readline().split())

def dijkstra(start, target):
    if start == target: #-- 만약 시작과 타겟이 같으면 걍 종료
        return 0
    distance = [INF] * (node+1)
    distance[start] = 1
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dis, nnode = heapq.heappop(q)
        if distance[nnode] < dis:
            continue
        for data in graph[nnode]:
            cost = dis + data[1]    
            if cost < distance[data[0]] :
                distance[data[0]] = cost
                heapq.heappush(q, (cost, data[0]))
    return distance[target]

cond1 = dijkstra(1, first_node) + dijkstra(first_node, second_node)\
        + dijkstra(second_node, node)
#-- case1 주어진 노드 중 v1을 먼저 탐색하고 v2를 나중에 탐색하는 방법

cond2 = dijkstra(1, second_node) + dijkstra(second_node, first_node)\
        + dijkstra(first_node, node)
#-- case2 주어진 노드 중  v2를 먼저 탐색하고 v1를 나중에 탐색하는 방법 

answer = min(cond1, cond2)
#-- case1과 case2 중 더 빠른 경로 탐색

if answer >= INF:
    print(-1)
else:
    print(answer)