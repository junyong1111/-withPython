import sys
from collections import deque
sys.stdin = open("8.그래프이론/input.txt")

node, edge = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node+1)]
indegree = [0] *(node+1)

for _ in range(edge):
    fromNode, toNode = map(int, sys.stdin.readline().split())
    graph[fromNode].append(toNode)
    indegree[toNode] +=1 


def topology_sort():
    ret = []
    q = deque()
    
    for i in range(1, node+1):  #-- 진입차수가 0인 노드 삽입
        if indegree[i] == 0 :
            q.append(i)
    while q:
        curr_node = q.popleft()
        ret.append(curr_node)
        
        for data in graph[curr_node]:
            indegree[data] -= 1
            if indegree[data] == 0:
                q.append(data)
    return ret
result = topology_sort()

for ret in result:
    print(ret, end= ' ')