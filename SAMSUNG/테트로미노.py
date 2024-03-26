import sys
sys.stdin = open("SAMSUNG/input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())

#-- 90 회전 로직
#-- x,y = [N-X-1][Y]

#-- 위아래 대칭 로직
#-- X, Y => [X][N-Y-1]

