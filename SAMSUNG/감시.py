import sys
import copy
# sys.stdin = open("SAMSUNG/input.txt")
input = sys.stdin.readline

def myprint(arr, n, m, cctv):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print(" == == == ")
    
    print(cctv)
    print("=== MY PRINT === ")

N, M = map(int, input().split())

office = []
CCTV = []

for i in range(N):
    office.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] < 6:
            CCTV.append([j, i, office[i][j]])
# myprint(office, N, M, CCTV)
# -- init()

def detectingMap(Map, n, m):
    ret = 0
    for i in range(n):
        for j in range(m):
            if Map[i][j] == 0:
                ret +=1
    return ret
                
def ccvtNumberOne(x, y, move, newOffice):
    moving = [[(-1, 0)],[(1, 0)],[(0, -1)], [(0, 1)]]
    #-- 좌, 우, 상, 하
    
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
            nx += moving[move][m][0]
            ny += moving[move][m][1]


def ccvtNumberTwo(x, y, move, newOffice):
    moving = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
        
def ccvtNumberThree(x, y, move, newOffice):
    moving = [[(0, -1), (1, 0)], [(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]]
    #-- 상우, 우하, 하좌, 상좌
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            

def ccvtNumberFour(x, y, move, newOffice):
    moving = [[(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)]]
    #-- 좌상우, 상우하, 우하좌, 하좌상
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
        
def ccvtNumberFive(x, y, move, newOffice):
    moving = [[(0, -1), (0, 1), (-1, 0), (1, 0)]]
    #-- 상하좌우
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
                
possibleCCTVmove = [0, 4, 2, 4, 4, 1]
answer = 64
cctvLen = len(CCTV)
def backtracking(level, myoffice):
    global answer
    if level == cctvLen:
        ret = detectingMap(myoffice, N, M)
        answer = min(answer, ret)
        return
    saveOffice = copy.deepcopy(myoffice)
    x, y, cctvnumber = CCTV[level]
    
    for dir in range(possibleCCTVmove[cctvnumber]):
        if cctvnumber == 1:
            ccvtNumberOne(x, y, dir, saveOffice)
        elif cctvnumber == 2:
            ccvtNumberTwo(x, y, dir, saveOffice)
        elif cctvnumber == 3:
            ccvtNumberThree(x, y, dir, saveOffice)
        elif cctvnumber == 4:
            ccvtNumberFour(x, y, dir, saveOffice)
        elif cctvnumber == 5:
            ccvtNumberFive(x, y, dir, saveOffice)
        #-- 4번 
        backtracking(level+1, saveOffice)
        saveOffice = copy.deepcopy(myoffice)
    


backtracking(0, office)
print(answer)




