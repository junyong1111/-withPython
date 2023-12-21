import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")
MAX_SIZE = 10001
n = int(sys.stdin.readline())
wine = [0]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))
if n<=1:
    print(wine[1])
    sys.exit()
dp = [0] * MAX_SIZE
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]
if n<=2:
    print(dp[n])
    sys.exit()

dp[3] = max(dp[1]+ wine[3] , wine[2]+ wine[3] , dp[2])
for i in range(4, n+1):
    dp[i] =  max(dp[i-2]+ wine[i], wine[i-1]+dp[i-3]+ wine[i], dp[i-1]) 
    '''
    현재 포도주를 마시는 경우
    - 현재 포도주를 마시고 이전 포도주 + 3칸 떨어진 최대 포도주 
    - 현재 포도주를 마시고 2칸 떨어진 최대 포도주 마심
    현재 포도주를 마시지 않는 경우
    - 이전 포도주의 최대값을 가져옴
    '''
print(dp[n])