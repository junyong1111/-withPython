import sys
import heapq
# sys.stdin = open("input.txt")

node, edge = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
INF = int(1e9)
graph = [[] for _ in range(node+1)]

for i in range(edge):
    fromNode, toNode, weight = map(int, sys.stdin.readline().split())
    graph[fromNode].append((toNode, weight))
distance = [INF] * (node+1)

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dis, node = heapq.heappop(queue)
        # 만약 이미 저장된 데이터가 최단 경로면 패스
        if distance[node] < dis :
            continue
        for data in graph[node]:
            #-- 그래프는 현재 튜플 형태로 (노드, 가중치)
            #-- 1번 노드와 연결된 2번과 3번 노드의 비용 계산
            #-- dis는 1번 노드의 거리값이므로 
            #-- data1(2번 노드) = 2번노드, 가중치
            cost = dis + data[1] #-- 1번 + 2번 가중치를 cost에 넣고
            if cost < distance[data[0]] : #-- 최단 경로인 경우
                distance[data[0]] = cost #-- 최단 경로 갱신
                heapq.heappush(queue, (cost, data[0])) #-- 큐에다가 해당 노드 삽입


dijkstra(start)      

for i in range(1, node+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])