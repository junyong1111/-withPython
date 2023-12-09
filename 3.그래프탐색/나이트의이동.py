
import sys
from collections import deque
sys.stdin = open('3.그래프탐색/input.txt')

'''
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
'''
steps = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
testcase = int(sys.stdin.readline())

while testcase:
    testcase-=1
    
    n = int(sys.stdin.readline())
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    c_location, w_location = map(int, sys.stdin.readline().split())
    board[c_location] = 1
    q = deque()
    q.append((c_location))
    

    
    
    
    
    