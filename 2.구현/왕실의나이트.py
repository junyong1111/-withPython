import sys
import pprint

sys.stdin = open('2.구현/input.txt')

#-- 1. 수평으로 두 칸 이동 뒤에 수직으로 한 칸
#-- 2. 수직으로 두 칸 이동 뒤에 수평으로 한 칸



x, y = str(sys.stdin.readline())
x = ord(x) - ord('a') + 1
y = int(y)
cnt = 0
#-- 좌2 위1 좌2 아래 1 
#-- 우2 위1 우2 아래 1
#-- 아래2 좌1 아래2 우1
#-- 위2 좌1 위2 우1
steps =[(-2, -1), (-2, 1), (2, -1), (2, 1), (2, -1), (2, 1), (-2, -1), (-2, 1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    
    if (nx >=1 and nx <= 8) and (ny >=1 and ny <=8):
        cnt +=1

print(cnt)