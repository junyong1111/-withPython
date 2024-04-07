import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

def myprint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print("=== === ===")

def init(n):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    return arr

def prefix(grid, n):
    pre = [0]
    iidx = 0
    jidx = 0
    for _ in range((n*n)):
        # print("{} {} {}".format(iidx, iidx//(n), jidx%n))
        pre.append(pre[iidx-1] + grid[iidx//n][jidx%n])
        jidx+=1
        iidx+=1
    return pre

grid = init(N)
#-- init

#-- step1. 구간합 구하기
pre = prefix(grid, N)
# myprint(pre, N+1, N+1)

print(pre)
# for _ in range(M):
#     y1, x1, y2, x2 = map(int, input().split())
#     print(pre[(N*y2) + x2] - pre[(N*y1) + x1-1])
