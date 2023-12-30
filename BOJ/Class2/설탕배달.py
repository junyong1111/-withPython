import sys
# sys.stdin = open("Class2/input.txt")

# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
# 현재 가지고 있는 봉지는 3Kg, 5Kg 2개 뿐
weight = int(sys.stdin.readline())
INF = int(1e9)
MAX_SIZE = 5001
answer = 0
dp = [INF] * (MAX_SIZE)

dp[3] = 1
dp[5] = 1

for i in range(6, weight+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
    #-- 3kg 또는 5kg 둘 중 더 작은 봉지 +1
if dp[weight] >= INF:
    print(-1)
    sys.exit()
print(dp[weight])