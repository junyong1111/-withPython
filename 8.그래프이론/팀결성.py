import sys
sys.setrecursionlimit(100001)
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
        parent[b] = parent[a]

node, edge = map(int, sys.stdin.readline().split())
parent = [0] * (node+1)

for i in range(node+1):
    parent[i] = i

for _ in range(edge):
    f, a, b = map(int, sys.stdin.readline().split())
    if f == 0 :
        unionparent(parent, a, b)   
    else:
        a = findparent(parent, a)
        b = findparent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")