import sys
import math
# sys.stdin = open("BOJ/Class3/input.txt")
COUNT = 0
N, r, c = map(int, sys.stdin.readline().split())
if N == 0:
    print(0)
    sys.exit()
SIZE = round(math.pow(2, N))


def findZ(n, x, y):
    global COUNT
    if n == 0: #-- base
        if y == r and x == c:
            print(COUNT)
        COUNT+=1
        
      
    else:
        alpha = int(math.pow(2, n-1))
        findZ(n-1, x, y) #-- 좌상
        findZ(n-1, x+alpha, y) #-- 우상
        findZ(n-1, x, y+alpha) #-- 좌하
        findZ(n-1, x+alpha, y+alpha) #-- 우하
  
findZ(N, 0, 0)