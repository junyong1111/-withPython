import sys
sys.stdin = open("9.알고리즘유형별/그리디/input.txt")

'''
2 3 1 2 2
'''
n = int(sys.stdin.readline())
adventure = list(map(int, sys.stdin.readline().split()))
stack = sorted(adventure, reverse= True)

answer = 0
flag = False
while stack:
    
    data = stack.pop()
    for i in range(1, data):
        if stack and data==stack[-1]:
            stack.pop()
        else:
            flag = True
            break
    if flag == False:
        answer +=1
print(answer)