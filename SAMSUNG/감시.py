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
    
def backtracking(level, index, detect, oldOffice):
    newOffice = copy.deepcopy(oldOffice)
    #-- 만약에 현재 들어온 Index가 존재하는 CCTV보다 많은 경우에는 제외
    if index >= len(CCTV):
        return
    
    #-- step1. 현재 CCTV가 이동가능 한 횟수만큼 이동
    x, y, cctvNumber = CCTV[index]
    
    for move in range(possibleMove[cctvNumber]):
        #1번 CCTV 4방향 이동 가능
        if cctvNumber  == 1:
            ndetect = detect + detectOneCCTV(x, y, move, newOffice)
        #2번 CCTV 2방향 이동 가능
        elif cctvNumber == 2:
            ndetect = detect + detectTwoCCTV(x, y, move, newOffice)
        #3번 CCTV 4방향 이동 가능
        elif cctvNumber == 3:
            ndetect = detect + detectThreeCCTV(x, y, move, newOffice)
        #4번 CCTV 4방향    
        elif cctvNumber == 4:
            ndetect = detect + detectFourCCTV(x, y, move, newOffice)
        #5번 CCTV 이동 불가    
        elif cctvNumber == 5:
            ndetect = detect + detectFiveCCTV(x, y, move, newOffice)
        
        if index+1 == level:
            answerList.append(ndetect)
        #-- step3. 또 다른 CCTV 확인
        for i in range(index+1, len(CCTV)):
            if visit[i] == False:
                visit[i] = True
                backtracking(level+1, i, ndetect, newOffice)
                visit[i] = False

startNode = 0
visit = [False] * len(CCTV)
visit[startNode] = True

backtracking(1, startNode, 0, office)
emptySpace = 0
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            emptySpace+=1

print(emptySpace - max(answerList))
        