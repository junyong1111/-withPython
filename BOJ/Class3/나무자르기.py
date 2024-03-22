import sys
import math
# sys.stdin = open("BOJ/Class3/input.txt")

input = sys.stdin.readline
MAX_LEN = 1000000000

# print(math.log2(MAX_LEN)) 
#-- O(logN) 최대 30

N, Target = map(int, input().split())
Tree = list(map(int, input().split()))

left = 0 #-- 0부터 시작~
right = max(Tree)
answer = max(Tree)

while left <= right:
    height = (left+right) // 2
    # print("{} 크기 만큼 자름".format(height))
    #-- step1. 모든 나무를 반으로 자름
    total = 0
    for tree in Tree:
        total += max(0, tree-height)
    #-- O(N) 최대 N
    
    #-- step2. 잘려진 크기에 따라 분류
    # print("잘려진 모든 나무의 길이 {}".format(total))
    #-- step2-1 목표보다 더 많이 가졌으면 조금 더 높이 자름
    if total >= Target:
        answer = height
        left = height+1
        # print("너무 많이 남았다. 더 높이 잘라도 ㄱㅊ")
    
    #-- step2-2 목표보다 더 많이 적게 가졌으면 조금 더 낮게 자름
    elif total < Target:
        right = height-1
        # print("너무 적게 남았다. 더 낮게 잘라도 ㄱㅊ")
print(answer)