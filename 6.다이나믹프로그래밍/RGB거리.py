import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

houses = int(sys.stdin.readline())
rgb = [[0 for _ in range(3)] for _ in range(houses)]

for i in range(houses):
    data = sys.stdin.readline().split()
    for j in range(3):
        rgb[i][j] = int(data[j])
        
dp = [[0 for _ in range(3)] for _ in range(houses)]

dp[0][0] = rgb[0][0] # R
dp[0][1] = rgb[0][1] # G
dp[0][2] = rgb[0][2] # B

for house in range(1, houses):
    red = rgb[house][0]
    green = rgb[house][1]
    blue = rgb[house][2]
    
    dp[house][0] = min(red + dp[house-1][1], red + dp[house-1][2])
    dp[house][1] = min(green + dp[house-1][0], green + dp[house-1][2])
    dp[house][2] = min(blue + dp[house-1][1], blue + dp[house-1][0])

print(min(dp[houses-1]))