import sys
sys.setrecursionlimit(10001)
# sys.stdin = open("8.그래프이론/input.txt")

def findparent(parent, node):
    if parent[node] != node:
        parent[node] = findparent(parent, parent[node])
    return parent[node]

def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]
        
node, edges = map(int, sys.stdin.readline().split())
parent = [0] * (node+1)
for i in range(node+1):
    parent[i] = i
edgetable = []

for _ in range(edges):
    a, b, cost = map(int, sys.stdin.readline().split())
    edgetable.append((a, b, cost))
edgetable = sorted(edgetable, key = lambda e : e[2])

ret = 0
for edge in edgetable:
    a, b, cost = edge
    if findparent(parent, a) == findparent(parent, b):
        continue
    unionparent(parent, a, b)
    ret += cost
print(ret)