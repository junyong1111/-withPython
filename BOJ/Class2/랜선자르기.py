import sys
# 최대 입력 제외 lonN
# sys.stdin = open("BOJ/Class2/input.txt")

N, K = map(int, sys.stdin.readline().split())
lans = []
for _ in range(N):
    lans.append(int(sys.stdin.readline()))

start  = 1
end = max(lans)

while start<end:
    # 경우도 포함되기 때문에 무한루프를 피하려면 +1을 여기서 해줘야 함 (반대로 하면 실패함)
    mid = (start+end) //2 +1
    cut = 0
    for lan in lans:
        cut += lan//mid
    if cut >= K : #-- 가능성 존재 
        start = mid
        # 같은 경우도 넣어주기 때문에 mid +1을 안한다.
    elif cut < K : #-- 너무 크게 잘랐음
        end = mid-1
print(start)