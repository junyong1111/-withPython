import sys
sys.stdin = open("9.알고리즘유형별/input.txt")

def myprint(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
        
def rotate90(arr, n):
    rotatearr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotatearr[i][j] = arr[n-j-1][i]
    return rotatearr
    

n = int(sys.stdin.readline())
Lock = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().split()
    for j in range(n):
        Lock[i][j] = int(data[j])

m = int(sys.stdin.readline())
Key = [[0 for _ in range(m)] for _ in range(m)]

for i in range(m):
    data = sys.stdin.readline().split()
    for j in range(m):
        Key[i][j] = int(data[j])


# moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1)]
moves = ["left", "right", "up", "down", "rotate"]

def moveLeft(Key):
    moveK = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m-1):
            moveK[i][j] = Key[i][j+1]
    for i in range(m):
        for j in range(m-1, m):
            moveK[i][j] = 0
    
    return moveK

def moveRight(Key):
    moveK = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(1, m):
            moveK[i][j] = Key[i][j-1]
    for i in range(m):
        for j in range(1):
            moveK[i][j] = 0
    return moveK

def moveUp(Key):
    moveK = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m-1):
        for j in range(m):
            moveK[i][j] = Key[i+1][j]
    for i in range(m-1, m):
        for j in range(m):
            moveK[i][j] = 0
    return moveK

def moveDown(Key):
    moveK = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, m):
            moveK[i][j] = Key[i-1][j]
    for i in range(1):
        for j in range(m):
            moveK[i][j] = 0
    return moveK
            
def getSum(arr, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt+=1
    return cnt
            
def moveKey(order, Key):
    if order =="left":
        moveKey = moveLeft(Key)   
        if getSum(moveKey, m) >= getSum(Lock, n):
            return moveKey
        else:
            return Key
    elif order =="right":
        moveKey = moveRight(Key)
        if getSum(moveKey, m) >= getSum(Lock, n):
            return moveKey
        else:
            return Key
    elif order =="up":
        moveKey = moveUp(Key)
        if getSum(moveKey, m) >= getSum(Lock, n):
            return moveKey
        else:
            return Key
    elif order =="down":
        moveKey = moveDown(Key)
        if getSum(moveKey, m) >= getSum(Lock, n):
            return moveKey
        else:
            return Key
    else:
        moveKey = rotate90(Key, m)
        if getSum(moveKey, m) >= getSum(Lock, n):
            return moveKey
        else:
            return Key
        
          
for move in moves:
    Key = moveKey(move, Key)
    if getSum(Key, m) >= getSum(Lock, n):
        
        
    
    
    
    


