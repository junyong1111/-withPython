import sys
import copy
sys.stdin = open("SAMSUNG/input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
office = []
CCTV = []
for i in range(N):
    office.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if office[i][j] >=1 and office[i][j] <=5:
            CCTV.append([j, i, office[i][j]])#-- x, y, CCTV 종류
def myprint():
    for i in range(N):
        for j in range(M):
            print(office[i][j], end=" ")
        print()
    print(CCTV)

# myprint()

possibleMove = [0, 4, 2, 4, 4, 1] 

def detectOneCCTV(x, y, move, newOffice):
    moving = [[(-1, 0)],[(1, 0)],[(0, -1)], [(0, 1)]]
    #-- 좌, 우, 상, 하
    dectedSpace = 0
    
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
                dectedSpace+=1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
    return dectedSpace



def detectTwoCCTV(x, y, move, newOffice):
    moving = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
    dectedSpace = 0
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
                dectedSpace+=1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
    return dectedSpace
        
def detectThreeCCTV(x, y, move, newOffice):
    moving = [[(0, -1), (1, 0)], [(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)]]
    #-- 상우, 우하, 하좌, 상좌
    dectedSpace = 0
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
                dectedSpace+=1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
    return dectedSpace

def detectFourCCTV(x, y, move, newOffice):
    moving = [[(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)]]
    #-- 좌상우, 상우하, 우하좌, 하좌상
    dectedSpace = 0
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
                dectedSpace+=1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
    return dectedSpace
        
def detectFiveCCTV(x, y, move, newOffice):
    moving = [[(0, -1), (0, 1), (-1, 0), (1, 0)]]
    #-- 상하좌우
    dectedSpace = 0
    for m in range(len(moving[move])):
        nx = x + moving[move][m][0]
        ny = y + moving[move][m][1]
        
        while 0 <= nx < M and 0 <= ny < N and newOffice[ny][nx] != 6:
            if newOffice[ny][nx] == 0:
                newOffice[ny][nx] = -1
                dectedSpace+=1
            nx += moving[move][m][0]
            ny += moving[move][m][1]
            
    return dectedSpace 
answerList = []

# x,y, cctv = CCTV[-1]
# for move in range(possibleMove[cctv]):
#     print(detectTwoCCTV(x, y, move))
    
def backtracking(index, office):
    global answer
    
    if index == len(CCTV):
        count = 0
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    count += 1
        answer = min(answer, count)
        return
    
    x, y, cctvNumber = CCTV[index]
    
    for move in range(possibleMove[cctvNumber]):
        newOffice = copy.deepcopy(office)
        
        if cctvNumber == 1:
            detectOneCCTV(x, y, move, newOffice)
        elif cctvNumber == 2:
            detectTwoCCTV(x, y, move, newOffice)
        elif cctvNumber == 3:
            detectThreeCCTV(x, y, move, newOffice)
        elif cctvNumber == 4:
            detectFourCCTV(x, y, move, newOffice)
        elif cctvNumber == 5:
            detectFiveCCTV(x, y, move, newOffice)
        
        backtracking(index + 1, newOffice)

startNode = 0
visit = [False] * len(CCTV)
visit[startNode] = True

answer = float('inf')
backtracking(0, office)
print(answer)
