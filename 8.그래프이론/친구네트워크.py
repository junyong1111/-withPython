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
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

testcase = int(sys.stdin.readline())

while testcase:
    testcase-=1
    node = int(sys.stdin.readline())
    
    dic = dict()
    cnt = 1
    for _ in range(node):
        f1, f2 = map(str, sys.stdin.readline().split())
        dic[f1] = cnt
        cnt +=1 
        dic[f2] = cnt
        cnt+1
    

        
        
        
    

