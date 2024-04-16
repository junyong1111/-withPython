import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline
nodes = int(input())

graph = [[] for _ in range(nodes+1)]

#-- 양방향 그래프 연결
for _ in range(nodes-1):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

#-- 부모노드에 대한 정보를 저장할 정답 배열 선언
answer = [0] * (nodes+1)

#-- BFS탐색
def bfs():
    visit = [False] * (nodes+1)
    queue = deque()
    queue.append(1)
    visit[1] = True
    #-- 루트 노드인 1번부터 시작
    
    while queue:
        node = queue.popleft()
        #-- 노드에 연결된 모든 노드들을 탐색
        for data in graph[node]:
            #-- 최초 방문이라면 해당 데이터의 부모는 현재 기준으로 삼고 있는 노드
            if visit[data] == False:
                answer[data] = node
                visit[data] = True
                queue.append(data)

#-- BFS 실행
bfs()
#-- 정답 출력
for target in range(2, (nodes+1)):
    print(answer[target])