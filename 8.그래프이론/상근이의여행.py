import sys
sys.setrecursionlimit(1001)
# sys.stdin = open("8.그래프이론/input.txt")

def findparent(parent, node):
    if parent[node] != node :
        parent[node] = findparent(parent , parent[node])
    return parent[node]

def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    if a < b :
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
        

testcase = int(sys.stdin.readline())
while testcase:
    testcase-=1
    n, m  = map(int, sys.stdin.readline().split())
    edges = []
    
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i
        
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a,b))
    
    ret = 0
    for edge in edges:
        a, b = edge
        if findparent(parent, a) == findparent(parent, b):
            continue
        unionparent(parent, a, b)
        ret +=1
    print(ret)