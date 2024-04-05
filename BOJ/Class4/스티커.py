import sys
# sys.stdin = open("BOJ/Class4/input.txt")
input = sys.stdin.readline

TWO = 2
testcase = int(input())

UP, DOWN = 0, 1

def init():
    arr = []
    for _ in range(TWO):
        arr.append(list(map(int, input().split())))
    return arr
            
def myPrint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end= " ")
        print()
    print("=== === === ")
while testcase:
    testcase-=1
    
    N = int(input())
    sticker = init()
    # myPrint(sticker, TWO, N)
    
    dp = [[0 for _ in range(N+1)] for _ in range(TWO)]
    dp[UP][1] = sticker[UP][0]
    dp[DOWN][1] = sticker[DOWN][0]
    
    if N <= 1:
        print(max(sticker[UP][0], sticker[DOWN][0]))
        continue
    
    dp[UP][2] = dp[DOWN][1] + sticker[UP][1]
    dp[DOWN][2] = dp[UP][1] + sticker[DOWN][1]
    
    for i in range(3, N+1):
        dp[UP][i] = max(dp[DOWN][i-1], dp[UP][i-2], dp[DOWN][i-2]) + sticker[UP][i-1]
        dp[DOWN][i] = max(dp[UP][i-1], dp[UP][i-2], dp[DOWN][i-2]) + sticker[DOWN][i-1]
        
    print(max(dp[UP][N], dp[DOWN][N]))
    # myPrint(dp, TWO, N+1)
    
    
    