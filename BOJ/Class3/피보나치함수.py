import sys
# sys.stdin = open("BOJ/Class3/input.txt")
MAX_SIZE = 41
testcase = int(sys.stdin.readline())

def cal(point1, point2):
    x = point1[0] + point2[0]
    y = point1[1] + point2[1]
    return [x, y]
    
dp = [[]] * MAX_SIZE
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, MAX_SIZE):
    dp[i] = cal(dp[i-1], dp[i-2])
    
while testcase:
    testcase-=1
    n = int(sys.stdin.readline())
    for data in dp[n]:
        print(data, end=" ")
    print()