import sys
sys.stdin = open("8.그래프이론/input.txt")

def findparent(parent, node):
    if parent[node] != node:
        parent[node] = findparent(parent, parent[node])
    return parent[node]

def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    if a < b :
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

node, edge = map(int, sys.stdin.readline().split())
parent = [0] * (node+1)

for i in range(node+1):
    parent[i] = i
    
edge_table = []
for _ in range(edge):
    a, b , cost = map(int, sys.stdin.readline().split())
    edge_table.append((a, b, cost))
    
edge_table = sorted(edge_table, key = lambda e : e[2])

ret = 0
last = 0
for e in edge_table:
    a, b, cost = e
    if findparent(parent, a) == findparent(parent, b):
        continue
    print("from node : {} to node : {} cna be unioed".format(a, b))
    unionparent(parent, a, b)
    ret += cost
    last = cost
print(ret - last)    