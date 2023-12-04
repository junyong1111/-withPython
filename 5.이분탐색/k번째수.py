import sys
# sys.stdin = open("5.이분탐색/input.txt")

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
#-- N = 3
#-- K = 7
#-- Answer = 6
# Answer = 6
# print("{} x {} 행렬에서 {} 보다 작거나 같은 데이터의 개수는 최소 {}개다.".format(N, N, Answer, K))

left = 1
right = N*N

def get_count(N, value):
    cnt = 0
    for i in range(1, N+1):
        cnt = cnt + min((value//i), N)
    return cnt
    
# value 6 
# 1 2 3 
# 2 4 6
# 3 6 9 

while left < right:
    mid = (left+right)//2
    
    cnt = get_count(N, value= mid)
    # print("mid : {} cnt : {}  we need to find values : [{}, {}]".format(mid, cnt, Answer, K))
    if K <= cnt: #-- 원하는 데이터의 개수 이상으로 나온 경우 사이즈를 줄여야 함
        # print("#-- 원하는 데이터의 개수 이상으로 나온 경우 사이즈를 줄여야 함")
        right = mid
        
    else: #-- 원하는 개수보다 적게 나온 경우 mid값을 올려야 함
        # print('#-- 원하는 개수보다 적게 나온 경우 mid값을 올려야 함')
        left = mid+1
    # print()
print(left)

