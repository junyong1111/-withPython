import sys
sys.stdin = open("8.그래프이론/input.txt")

def findParent(parent, node):
    if parent[node] != node:
        parent[node] = findParent(parent, parent[node])
    return parent[node]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    
    if a < b :
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

node, edges = map(int, sys.stdin.readline().split())
parent = [0] * (node+1)

edgeTable = []
for i in range(node+1):
    parent[i] = i
    
for _ in range(edges):
    a, b, cost = map(int, sys.stdin.readline().split())
    edgeTable.append((a,b,cost))

edgeTable = sorted(edgeTable, key = lambda edge : edge[2])
#-- 간선 비용 오름차순 정렬
ret = 0
for edge in edgeTable:
    a, b, cost = edge
    #-- 집합 확인 
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a == b:
        continue
    unionParent(parent, a, b)
    ret += cost
print(ret)   
    