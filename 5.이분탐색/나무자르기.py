import sys
# sys.stdin = open("5.이진탐색/input.txt")

N, target = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)

while left < right:
    mid = (left+right) // 2 +1
    total = 0
    for tree in trees:
        total += max(tree - mid, 0)
    if total < target:  #-- total이 작다는건 너무 크게 자름 끝자락을 더 줄여야 함
        right = mid -1
    else: #-- 필요한 만큼 찾은 경우 
        left = mid
print(left)