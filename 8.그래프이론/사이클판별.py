import sys
sys.setrecursionlimit(100)
sys.stdin = open("8.그래프이론/input.txt")

node, edge = map(int, sys.stdin.readline().split())
table = [0] * (node+1)

for i in range(node+1):
    table[i] = i 

def findParent(table, node):
    if table[node] != node:
        table[node] = findParent(table, table[node])
    return table[node]

def unionParent(a, b, table):
    a = findParent(table, a)
    b = findParent(table, b)
    
    if a < b:
        table[b] = a
    else:
        table[a] = b

cycle = False

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    if findParent(table, a) == findParent(table, b):
        cycle = True
        break
    else:
        unionParent(a, b, table)
    
if cycle == True:
    print("Cycle is true")
else:
    print("Cycles is false")
        