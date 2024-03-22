import sys
from collections import deque

sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
people = deque()
Exit = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#-- 상하좌우

def init():
    for i in range(1, N+1):
        data = input().split()
        for j in range(1, N+1):
            grid[i][j] = int(data[j-1])
            
    for i in range(M):
        people.append(list(map(int, input().split()))) #-- i j
    Exit.append((list(map(int, input().split()))))
        
            
def myprint():
    print("===== grid ====")
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(grid[i][j], end=" ")
        print()
    print("===== poeple ====")
    print(people)
    print("===== Exit ====")
    print(Exit)
        
#-- 거리 계산        
def distance(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])
#-- step1. 초기셋팅
init()
# myprint()

"""
룰 : 
1초마다 모든 참가자는 한 칸씩 움직입니다. 움직이는 조건은 다음과 같습니다.

두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의됩니다.
모든 참가자는 동시에 움직입니다.

1. 상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
2. 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
    - 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    
3. 참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
4. 한 칸에 2명 이상의 참가자가 있을 수 있습니다.
5. 모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전합니다.

6. 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
- 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
- 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.
"""

                    
                
        
    




        