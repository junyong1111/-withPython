'''
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
Left, Down, Right, Up

2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.

3. 만약 4방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을 멈춘다.

북쪽 0 
동쪽 1
남쪽 2
서쪽 3

육지 0
바다 1
'''

import sys
import pprint
sys.stdin = open('2.구현/input.txt')


def turnleft():
    global direction
    direction = direction +1 
    if direction == 4:
        direction = 0
    
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]    
    
#-- u, l, d, r

n,m = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())

gameMap = []
visit = [[0 for j in range(m)] for i in range(n)]
visit[y][x] = 1
for i in range(n):
    gameMap.append(list(map(int, sys.stdin.readline().split())))
answer = 1
turn_time = 0
while True:
    turnleft()
    ny = y + move[direction][1]
    nx = x + move[direction][0]
    if (ny >= 0 and ny < n) and(nx >=0 and nx < m) and (visit[ny][nx] ==0) and (gameMap[ny][nx] == 0):
        visit[ny][nx] = 1
        (x, y) = (nx, ny)
        answer += 1
        turn_time = 0
    else:
        turn_time +=1
    if turn_time == 4:
        ny = y - move[direction][1]
        nx = x - move[direction][0]
        if gameMap[ny][nx] == 0:
            (x, y) = (nx, ny)
            turn_time = 0
        else:    
            break
print(answer)