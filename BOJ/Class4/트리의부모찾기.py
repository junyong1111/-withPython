import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

nodes = int(input())

graph = [[] for _ in range(nodes+1)]
info = []

for _ in range(nodes-1):
    nodeA, nodeB = map(int, input().split())
    info.append([nodeA, nodeB])
    # graph[nodeA].append(nodeB)
    # graph[nodeB].append(nodeA)

info.sort(key=lambda node: node[0])
for i in range(len(info)):
    nodeA, nodeB = info[i]
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


for i in range(2, nodes+1):
    print(graph[i][0])
