import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))


def myPrint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()


# myPrint(city, N, N)
# -- init 확인

# -- 집에 대한 정보를 큐에
# -- 치킨 집에 대한 정보를 큐에 저장
house = deque()
chicken = deque()

for i in range(N):
    for j in range(N):
        # -- 집이면 집 큐에 추가
        if city[i][j] == 1:
            house.append([j, i])  # -- x y 좌표로
        # -- 치킨 집이면 치킨집 큐에 추가
        if city[i][j] == 2:
            chicken.append([j, i])  # -- X Y 좌표로


# -- 거리 계산 함수 정의
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# -- 백 트랙킹 시작
answer = []


# print(" Total House is {}".format(house))
# print(" Total Chicken House is {}".format(chicken))
def backtracking(level, index):
    if level == M:
        # -- 최단 거리
        ret = 0
        # -- 집을 다 돌면서 남은 치킨 집과의 최단 거리를 계산
        for h in house:
            shortestPath = INF
            for v in range(len(visit)):
                if visit[v] == True:
                    shortestPath = min(shortestPath, distance(h[0], h[1], chicken[v][0], chicken[v][1]))
            ret += shortestPath
        answer.append(ret)
        return

    for i in range(index + 1, len(chicken)):
        if not visit[i]:
            visit[i] = True
            backtracking(level + 1, i)
            visit[i] = False


visit = [False] * (len(chicken))
for i in range(len(chicken)):
    visit[i] = True
    backtracking(1, i)
    visit[i] = False

print(min(answer))
