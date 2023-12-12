import sys
sys.setrecursionlimit(1001)
sys.stdin = open("8.그래프이론/input.txt")

def findparent(parent, node):
    if parent[node] != node:
        parent[node] = findparent(parent, parent[node])
    return parent[node]

def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
        

stars = int(sys.stdin.readline())
parent = [0] * (stars+1)
for i in range(stars+1):
    parent[i] = i

edges = []

point = []
for _ in range(stars):
    a, b = map(float, sys.stdin.readline().split())
    point.append((a,b))

costs = []
fx, fy = point[0]
for i in range(1, stars):
    x, y = point[i]
    cost = pow(pow((fx - x),2) + pow(abs(fy - y),2), 0.5)
    costs.append(cost)
    fx, fy = x,y
x, y = point[0]
cost = pow(pow((fx - x),2) + pow(abs(fy - y),2), 0.5)
costs.append(cost)

idx = 1
for i in range(len(costs)-1):
    edges.append((idx, idx+1, costs[i]))
    idx+=1 
edges.append((idx, 1, costs[-1]))

edges = sorted(edges, key = lambda e : e[2])
ret = 0
for edge in edges:
    a, b, cost = edge
    if findparent(parent, a) == findparent(parent, b):
        continue
    unionparent(parent, a, b)
    ret += cost
print(round(ret, 2))