import sys
# sys.stdin  = open("BOJ/Class3/input.txt")

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
priority = list(zip(arr, range(1, n+1)))

#-- 가장 빠르게 끝나는 작업을 우선적으로 그리디 하게 탐색
priority.sort(key=lambda x : x[0])
answer = 0 
time = 0
for pri in priority: 
    time = time + pri[0]
    answer += time 
print(answer)