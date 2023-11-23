import sys
import pprint
sys.stdin = open('2.구현/input.txt')


n = int(sys.stdin.readline())
# Map = [[0 for j in range(n+1)] for i in range(n+1)]
plans = str(sys.stdin.readline()).split()


x = 1
y = 1

for plan in plans:
    if plan == 'R' and x+1 <= n:
        x +=1
        continue
    if plan == 'L' and x-1 >= 1:
        x-= 1
        continue
    if plan == 'U' and y-1 >= 1:
        y-= 1
        continue
    if plan == 'D' and y+1 <= n:
        y += 1
        continue
print(y, x)
        
    





