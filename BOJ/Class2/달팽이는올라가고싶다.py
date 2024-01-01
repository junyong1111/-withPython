import sys
import math
# sys.stdin = open("BOJ/Class2/input.txt")

A, B, V = map(int, sys.stdin.readline().split())


#-- (V-B)는 마지막 날에 달팽이가 올라야 할 남은 높이
#-- (A-B)는 달팽이가 하루 동안 실제로 올라가는 높이 
day = (V-B) / (A-B) 



if day == int(day):
    # day가 정수라면, 정확히 그 날에 목표에 도달하는 것이므로 그대로 day를 출력
    print(int(day))
else:
    # day가 3.5일과 같이 정수가 아니라면 
    # 달팽이는 추가로 하루가 더 필요하므로 day를 올림하여 출력
    print(int(day)+1)