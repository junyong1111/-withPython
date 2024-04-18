import sys
# sys.stdin = open("BOJ/Class4/input.txt")
input = sys.stdin.readline

INF = int(1e9)

numberOfcity = int(input())
numberOfbus = int(input())

def myprint(arr, n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] >= INF:
                print(0, end=" ")
            else:
                print(arr[i][j], end=" ")
        print()
    

graph = [[INF for _ in range(numberOfcity+1)] for _ in range(numberOfcity+1)]

for i in range(1, numberOfcity+1):
    for j in range(1, numberOfcity+1):
        if i == j:
            graph[i][j] = 0

for _ in range(numberOfbus):
    start, end, weight = map(int, input().split())
    graph[start][end] = min(weight, graph[start][end])


for k in range(1, numberOfcity+1):
    for start in range(1, numberOfcity+1):
        for end in range(1, numberOfcity+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
            
myprint(graph, numberOfcity, numberOfcity)
