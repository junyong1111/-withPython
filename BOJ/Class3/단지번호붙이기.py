import sys
# sys.stdin = open("BOJ/Class3/input.txt")

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):
    data = sys.stdin.readline().strip()
    for j in range(N):
        graph[i][j] = int(data[j])

def dfs(x, y, N):
    stack = []
    stack.append((x, y))
    cnt = 1
    while stack:
        x,y = stack.pop()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0<=nx<N and 0<=ny<N and graph[ny][nx] == 1:
                cnt +=1
                graph[ny][nx] = 0
                stack.append((nx, ny))
    return cnt
   
answer = []

                
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            answer.append(dfs(j, i, N))
            
print(len(answer))
answer.sort()
for ans in answer:
    print(ans)