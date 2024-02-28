import sys
# sys.stdin = open("BOJ/Class3/input.txt")

testcase = int(sys.stdin.readline())
moves = [(0,1), (0,-1), (1,0), (-1, 0)]


def myPrint(arr, N, M):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end=" ")
        print()

def dfs(graph, N, M, x, y):
    stack = []
    stack.append((x, y))
    graph[y][x] = 0
    while stack:
        x, y = stack.pop()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1:
                stack.append((nx, ny))
                graph[ny][nx] = 0
        
while(testcase):
    testcase-=1
    answer = 0
    M, N, K  = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                answer +=1
                dfs(graph, N, M, j, i)
    print(answer)