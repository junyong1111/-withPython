import sys
import copy
# sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline


class myData():
    score = 0
    isSum = False
    
    def __init__(self, score):
        self.score = int(score)


def mydataPrint(board):
    for i in range(N):
        for j in range(N):
            print("{} {}".format(board[i][j].score, board[i][j].isSum), end= " ")
        print()
    

N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(myData, input().split())))


direction = ["U", "D", "L", "R"]
answerList = []

def findMax(board):
    maxValue = 0
    for i in range(N):
        for j in range(N):
            maxValue = max(maxValue, board[i][j].score)
    return maxValue

def reset(board):
    for i in range(N):
        for j in range(N):
            board[i][j].isSum = False
    return board
def moveup(OldBoard):
    newBoard = OldBoard
    
    dir = -1
    
    for y in range(N):
        for x in range(N):
            target = newBoard[y][x].score
            if target == 0:
                continue
            ny = y + dir
            while 0 <= ny < N: #--  범위 체크
                #-- 1. 이동할 수 있는 0이 있는 공간
                if newBoard[ny][x].score == 0:
                    newBoard[ny][x] = newBoard[ny-dir][x] #-- 이전 데이터 가져오고 삭제
                    newBoard[ny-dir][x] = myData(0)
                    ny += dir
                #-- 2. 나랑 같은 숫자
                elif newBoard[ny][x].score == target:
                    #-- -> 같은 숫자이지만 이미 합쳐진 경우
                    if newBoard[ny][x].isSum == True:
                        break
                    #-- -> 같은 숫자이고 처음 합쳐진 경우
                    else:
                        newBoard[ny][x].score *=2
                        newBoard[ny][x].isSum = True
                        newBoard[ny-dir][x] = myData(0)
                        break
                    
                #-- 3. 이동할 수 없는 다른 숫자
                else:
                    break
    return reset(newBoard)
                
                
def movedown(OldBoard):
    newBoard = OldBoard
    dir = 1
    
    for y in reversed(range(N)):
        for x in range(N):
            target = newBoard[y][x].score
            if target == 0:
                continue
            ny = y + dir
            while 0 <= ny < N: #--  범위 체크
                #-- 1. 이동할 수 있는 0이 있는 공간
                if newBoard[ny][x].score == 0:
                    newBoard[ny][x] = newBoard[ny-dir][x] #-- 이전 데이터 가져오고 삭제
                    newBoard[ny-dir][x] = myData(0)
                    ny += dir
                #-- 2. 나랑 같은 숫자
                elif newBoard[ny][x].score == target:
                    #-- -> 같은 숫자이지만 이미 합쳐진 경우
                    if newBoard[ny][x].isSum == True:
                        break
                    #-- -> 같은 숫자이고 처음 합쳐진 경우
                    else:
                        newBoard[ny][x].score *=2
                        newBoard[ny][x].isSum = True
                        newBoard[ny-dir][x] = myData(0)
                        break
                    
                #-- 3. 이동할 수 없는 다른 숫자
                else:
                    break
    return reset(newBoard)          
                
def moveleft(OldBoard):
    newBoard = OldBoard
    dir = -1
    
    for y in range(N):
        for x in range(N):
            target = newBoard[y][x].score
            if target == 0:
                continue
            nx = x + dir
            while 0 <= nx < N: #--  범위 체크
                #-- 1. 이동할 수 있는 0이 있는 공간
                if newBoard[y][nx].score == 0:
                    newBoard[y][nx] = newBoard[y][nx-dir] #-- 이전 데이터 가져오고 삭제
                    newBoard[y][nx-dir] = myData(0)
                    nx += dir
                #-- 2. 나랑 같은 숫자
                elif newBoard[y][nx].score == target:
                    #-- -> 같은 숫자이지만 이미 합쳐진 경우
                    if newBoard[y][nx].isSum == True:
                        break
                    #-- -> 같은 숫자이고 처음 합쳐진 경우
                    else:
                        newBoard[y][nx].score *=2
                        newBoard[y][nx].isSum = True
                        newBoard[y][nx-dir] = myData(0)
                        break
                    
                #-- 3. 이동할 수 없는 다른 숫자
                else:
                    break
    return reset(newBoard)
    
def moveright(OldBoard):
    newBoard = OldBoard
    dir = 1
    
    for y in range(N):
        for x in reversed(range(N)):
            target = newBoard[y][x].score
            if target == 0:
                continue
            nx = x + dir
            while 0 <= nx < N: #--  범위 체크
                #-- 1. 이동할 수 있는 0이 있는 공간
                if newBoard[y][nx].score == 0:
                    newBoard[y][nx] = newBoard[y][nx-dir] #-- 이전 데이터 가져오고 삭제
                    newBoard[y][nx-dir] = myData(0)
                    nx += dir
                #-- 2. 나랑 같은 숫자
                elif newBoard[y][nx].score == target:
                    #-- -> 같은 숫자이지만 이미 합쳐진 경우
                    if newBoard[y][nx].isSum == True:
                        break
                    #-- -> 같은 숫자이고 처음 합쳐진 경우
                    else:
                        newBoard[y][nx].score *=2
                        newBoard[y][nx].isSum = True
                        newBoard[y][nx-dir] = myData(0)
                        break
                    
                #-- 3. 이동할 수 없는 다른 숫자
                else:
                    break
    return reset(newBoard)
    
def findMaxScore(dir, turn, board):
    if turn > 5:
        answerList.append(findMax(board))
        return
    
    #-- 4방향 처리
    newBoard = copy.deepcopy(board)
    
    if dir =="U":
        newBoard = moveup(newBoard)
    elif dir =="D":
        newBoard = movedown(newBoard)
    elif dir =="L":
        newBoard = moveleft(newBoard)
    elif dir =="R":
        newBoard = moveright(newBoard)
    
    for dir in direction:
        findMaxScore(dir, turn+1, newBoard)
        
for dir in direction:
    myBoard = grid
    findMaxScore(dir, 1, myBoard)
    
print(max(answerList))    