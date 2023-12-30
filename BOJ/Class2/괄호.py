import sys
# sys.stdin = open("Class2/input.txt")

testCase = int(sys.stdin.readline())

while testCase:
    testCase-= 1
    stack = []
    ps = list(sys.stdin.readline().strip())
    flag = False
    for data in ps:
        if data == '(': #-- 정상적인 괄호는 삽입
            stack.append(data)
        else:
            if len(stack) == 0: #-- 괄호의 짝이 안맞다면 중단
                flag = True
                break
            else : 
                stack.pop()
    
    if len(stack) != 0 or flag: #-- 스택에 원소가 있거나 짝이 안맞은 경우
        print("NO")
    else:
        print("YES")
            
            
    
    