import sys
from enum import Enum
# sys.stdin = open("BOJ/Class3/input.txt")
input = sys.stdin.readline

def init(N):
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    return arr

def myPrint(arr ,n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print("----- Data -----")


class Color(Enum):
    WHITE = 0
    BLUE = 1
        
N = int(input())
grid = init(N)
#-- init --- 

blue = 0
white = 0


""" 
# -- step1. 현재 색종이가 모두 같은 색이라면 그냥 해당 색상 하나 증가
# -- step2. 같은 색이 아니라면 아래 로직에 따라 수행
1. 4등분 
2. 다시 step1
3. 만약 현재 색종이가 1개뿐이라면 종료

정리
BaseCase 
- N == 1 -> 현재 색상 반환
Recursion Step
- if step1 -> 해당 생삭 반환
- else 4분등 하여 다시 진행
"""

def isSameColor(x, y, n, target):
    for i in range(y, n+y):
        for j in range(x, n+x):
            if grid[i][j] != target:
                return False
    return True

def IncreaseContetti(target):
    global white, blue 
    if target == Color.BLUE.value:
        blue += 1
    elif target == Color.WHITE.value:
        white += 1

def MakeConfetti(x, y, n):
    
    # -- basecase 
    if n == 1:
        IncreaseContetti(grid[y][x])
        return

    # -- recursion step
    # -- step1 모두 같은 생삭
    if isSameColor(x, y, n, grid[y][x]) == True:
        IncreaseContetti(grid[y][x])
        return
    
    # -- step2 4등분 해서 다시 탐색
    harf = n//2
    MakeConfetti(x, y, harf) # -- 현재 좌표 그대로 -> 크기만 반으로 
    MakeConfetti(x+harf, y, harf) # -- x 좌표만 절반만큼 이동
    MakeConfetti(x, y+harf, harf) # -- y 좌표만 절반만큼 이동
    MakeConfetti(x+harf, y+harf, harf) #-- 모두 절반만큼 이동
    
MakeConfetti(0, 0, N)
print(white)
print(blue)
