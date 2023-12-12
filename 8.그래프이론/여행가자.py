import sys
sys.setrecursionlimit(10000)
# sys.stdin = open('8.그래프이론/input.txt')

def findparent(parent, node):
    if parent[node] != node :
        parent[node] = findparent(parent, parent[node])
    return parent[node]

def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    if a < b :
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
    

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    data = sys.stdin.readline().split()
    
    for j in range(1, len(data)+1):
        if i != j and int(data[j-1]) == 1:
            if findparent(parent, i) != findparent(parent, j):
                unionparent(parent, i, j)
        
travel = list(sys.stdin.readline().split())
compare = findparent(parent, int(travel[0]))

flag = False
for i in range(1, len(travel)):
    if compare != findparent(parent, int(travel[i])):
        flag = True
        break

if flag == False:
    print("YES")
else:
    print("NO")