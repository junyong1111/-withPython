import sys
# sys.stdin = open('BOJ/Class2/input.txt')

N, M, B = map(int, sys.stdin.readline().split())
grid = [list(map(int,input().split())) for _ in range(N)]

# 높이별 블록 수를 저장하는 딕셔너리 초기화
height_count = {}
for row in grid:
    for height in row:
        if height in height_count:
            height_count[height] += 1
        else:
            height_count[height] = 1

# 모든 가능한 높이에 대해 계산
min_time = int(1e9)
best_height = 0
min_block = min(map(min, grid))
max_block = max(map(max, grid))

for target_height in range(min_block, max_block+1):
    time = 0
    inventory = B
    for height, count in height_count.items():
        if height < target_height:
            # 블록 추가: 현재 높이가 목표 높이보다 낮은 경우
            time += (target_height - height) * count
            inventory -= (target_height - height) * count
        elif height > target_height:
            # 블록 제거: 현재 높이가 목표 높이보다 높은 경우
            time += 2 * (height - target_height) * count
            inventory += (height - target_height) * count

    if inventory >= 0 and time <= min_time:
        min_time = time
        best_height = target_height

print(min_time, best_height)

