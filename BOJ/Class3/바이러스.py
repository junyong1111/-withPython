import sys
# sys.stdin = open("BOJ/Class3/input.txt")

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[] for _ in range(node+1)]

for _ in range(edge):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
virus = [False] * (node+1)
stack = []

virus[1] = True
stack.append(1)

while stack:
    computer = stack.pop()
    for data in graph[computer]:
        if virus[data] == False:
            virus[data] = True
            stack.append(data)
cnt = -1 #-- 1번 컴은 제외
for data in virus:
    if data == True:
        cnt+=1
print(cnt)