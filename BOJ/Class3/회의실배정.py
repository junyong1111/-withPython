import sys
# sys.stdin = open("BOJ/Class3/input.txt")

n = int(sys.stdin.readline())
MAX_SIZE = 100001
rooms = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    rooms.append((a,b))

rooms.sort(key=lambda x : (x[1], x[0]))
#-- 종료시간이 같다면 시작시간이 빠른순서

_, end = rooms[0]
answer = 1

for i in range(1, n):
    if end <= rooms[i][0]:
        answer +=1
        _, end = rooms[i]
print(answer)