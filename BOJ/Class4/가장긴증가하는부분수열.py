import sys
from collections import deque
sys.stdin = open("BOJ/Class4/input.txt")

MAX_SIZE = 1001

N = int(sys.stdin.readline())
numbers = deque(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(MAX_SIZE)] for _ in range(4)]

#-- init()

dp[0][1] = numbers.popleft()
dp[1][1] = 0
dp[2][1] = dp[0][1]
dp[3][1] = 0


selectCnt = 1
nonSelectCnt = 0

for i in range(2, N+1):
    value = numbers.popleft()
    if dp[2][i-1]<value:
        dp[2][i] = value
        dp[0][i] = dp[0][i-1] + value 
        selectCnt+=1
        
        dp[3][i] = dp[3][i-1]
        dp[1][i] = dp[1][i-1]
    
    elif dp[3][i-1] < value:
        dp[3][i] = value
        dp[1][i] = dp[1][i-1] + value
        nonSelectCnt +=1
        
        dp[2][i] = dp[2][i-1]
        dp[0][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1]
        dp[1][i] = dp[1][i-1]
        dp[2][i] = dp[2][i-1]
        dp[3][i] = dp[3][i-1]
    
def myPrint():
    for i in range(4):
        for j in range(1,N+1):
            print(dp[i][j], end=" ")
        print()

myPrint()
print(max(selectCnt, nonSelectCnt))