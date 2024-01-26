import sys

def myPrint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()
N, M, B = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))


def isPossible():
    target = grid[0][0]
    for i in range(N):
        for j in range(M):
            if target != grid[i][j]:
                return False
    return True

def findmaxValue():
    max_value = 0
    for i in range(N):
        for j in range(M):
            max_value = max(max_value, grid[i][j])
    return max_value

def findMode():
    ground = [0] * 300
    for i in range(N):
        for j in range(M):
            ground[grid[i][j]] +=1
    return ground.index(max(ground))
          
def maxBolck():
    time = 0
    block =0
    max_value = findmaxValue()
    for i in range(N):
        for j in range(M):
            block += max_value - grid[i][j] 
            time += 1 * (max_value - grid[i][j] )
    return block, time

def modeBlock():
    time = 0
    block = 0
    remove_block = 0
    mode_value = findMode()
    for i in range(N):
        for j in range(M):
            temp = mode_value - grid[i][j]
            if (temp)>=0: #-- 벽돌을 설치 해야함
                block += temp
                time += 1 * temp
            else: #-- 벽돌을 제거해야 함
                temp = temp *-1
                block += temp
                time += 2 * temp
                remove_block+=1
    return block, time, remove_block

def removeBlock(mode):
    cnt = 0
    if mode == "max":
        max_value = findmaxValue()
        for i in range(N):
            for j in range(M):
                grid[i][j] = max_value
    elif mode == "mode":
        mode_value = findMode()
        for i in range(N):
            for j in range(M):
                grid[i][j] = mode_value
    else:
        max_value = findmaxValue()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == max_value:
                    grid[i][j] -=1
                    cnt +=1
    return cnt
                   
"""
1. 최댓값을 기준으로 맞출 때 필요한 블록과 시간을 계산
2. 최빈값을 기준으로 맞출 때 필요한 블록과 시간을 계산
3. 
if 2개 모두 가능성 없으면 최댓값을 기준으로 1개씩 내려감
else : 
3-1. 2개의 방법 중 최소 시간으로 진행
4. 모든 땅이 고르다면 종류
"""

total_time = 0
cnt = 0
while True:
    if isPossible():
        break
    #-- strp3-1. 나머지 블록으로 최댓ㄱ밧을 맞추는 경우
    max_block, max_time = maxBolck()
    if max_block>B: #-- 현재 가지고 있는 블록으로 커버가 안되는 경우는 넘어가야 함
        max_time = int(1e9)
        pass
    #-- strp3-2. 나머지 블록으로 최빈값을 맞추는 경우
    mode_block, mode_time, remove_block = modeBlock()
    if mode_block >B:
        mode_time = int(1e9)
        pass
    #-- 두 방법 중 최소로
    if max_time == mode_time and max_time == int(1e9):
        #-- 블록 자체가 부족한 경우 벌목 고고
        cnt = removeBlock("none")
        total_time += 2 * cnt
        B += cnt
        continue
    if mode_time < max_time:
        total_time += mode_time
        B += remove_block
        B -= mode_block
        removeBlock("mode")
    else:
        total_time += max_time
        B -= max_block
        removeBlock("max")
print(total_time, grid[0][0])