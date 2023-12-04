import sys
sys.stdin = open("5.이진탐색/input.txt")
have_k, need_n = map(int, sys.stdin.readline().split())
items = []
for i in range(have_k):
    items.append(int(sys.stdin.readline()))

left = 1
right = max(items)

while left < right:
    mid =  (left + right) // 2 +1 #-- 2. (1)에서 같은 경우도 포함되기 때문에 무한루프를 피하려면 +1을 여기서 해줘야 함 (반대로 하면 실패함)
    total = 0
    for item in items:
        total += item // mid
    if total >= need_n: #-- 가능성 존재
        left = mid #--1.  같은 경우도 넣어주기 때문에 mid +1을 안한다.
    elif total < need_n: #-- 너무 크게 잘랐음
        right = mid-1
print(left)