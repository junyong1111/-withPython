import sys
from collections import deque
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue)!=1:
    #-- step1 : 최상단을 버림
    queue.popleft()
    #-- step2 : 최상단을 맨 뒤로
    queue.append(queue.popleft())
    
print(queue[0])