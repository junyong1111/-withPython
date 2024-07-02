def solution(s):
    answer = 0
    for i in range(len(s)): # 회전 연산
        stack_s = [] #초기화
        stack_m = []
        stack_l = []
        flag = True
        k = s[i:]+s[:i] # 회전 문자열
        print(k)
        for j in k: # 각 케이스에 대한 스택 연산
            if j == '[':
                stack_l.append('[')
            elif j == '(':
                stack_s.append('(')
            elif j == '{':
                stack_m.append('{')
            elif j == ']':
                try:
                    stack_l.pop()
                except:
                    flag = False
                    break
            elif j == '}':
                try:
                    stack_m.pop()
                except:
                    flag = False
                    break
            elif j ==')':
                try:
                    stack_s.pop()
                except:
                    flag = False
                    break
        if len(stack_s) == 0 and len(stack_m) == 0 and len(stack_l) == 0 and flag == True:
            answer += 1
    return answer
