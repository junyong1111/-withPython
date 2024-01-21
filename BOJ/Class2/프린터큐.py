import sys
from collections import deque

# sys.stdin = open("BOJ/Class2/input.txt")
test_case = int(sys.stdin.readline())
while test_case:
    test_case-=1
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split())) #-- 우선순위 리스트
    ppq = deque() #-- 인덱스 + 우선순위 리스트
    trace = [] #-- 우선순위 출력 리스트
    for i in range(N):
        ppq.append((i, priority[i]))

    while ppq: 
        index, pri = ppq.popleft()
        if pri == max(priority): #-- 우선순위가 가장 높으면
            trace.append(index) #-- 정답 출력에 포함
            priority.pop(priority.index(max(priority))) #-- 해당 노드 삭제
        else:    
            ppq.append((index, pri))    #-- 뒤에 붙이기 
        
    print(trace.index(M)+1)