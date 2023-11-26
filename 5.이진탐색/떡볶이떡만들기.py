import sys
import bisect

sys.stdin = open("5.이진탐색/input.txt")
n, m = map(int, sys.stdin.readline().split())
rice_cakes = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(rice_cakes)

while left < right:
    mid = (left+right)//2
    #-- 시작점 0 끝점 19 중앙 9에서 떡을 잘라야
    ret = []
    for rice_cake in rice_cakes:
        ret.append(max(0, rice_cake - mid))
    if sum(ret) > m: #-- 너무 작게 썰었음
        left = mid + 1
    elif sum(ret) < m : #-- 너무 크게 썰었음
        right = mid -1
    else:
        print(mid)
        break
        
        
        