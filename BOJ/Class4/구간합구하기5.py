import sys
sys.stdin = open("BOJ/Class4/input.txt")

N, M = map(int, input().split())

original = []
for _ in range(N):
    original.append(list(map(int, input().split())))

#-- 2x2 구간합
prefix = [0] * ((N*N)+1)
start = 1

for i in range(N):
    for j in range(N):
        prefix[start] = original[i][j] + prefix[start-1]
        start+=1

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    
    right = ((y2 * N) - (N-1)) + (x2-1)
    left = ((y1 * N) - (N-1)) + (x1-1) -1
    print(prefix[right] - prefix[left])
    
#-- 이해를 잘못한듯 다시 도전 