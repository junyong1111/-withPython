import sys
# sys.stdin = open("input.txt")
# 0.5초 k랑 n이 상당히 작네 
MAX_N = 15
MAX_K = 15
test_case = int(sys.stdin.readline())

while test_case:
    test_case-=1
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    house = [[0 for _ in range(MAX_N)] for _ in range(MAX_K)] 
    for i in range(1, MAX_K):
        house[0][i] = i
    
    for i in range(1, K+1):
        for j in range(1, MAX_N):
            people = 0
            for k in range(1, j+1):
                people += house[i-1][k]
            house[i][j] = people
    print(house[K][N])