import sys
sys.stdin = open("9.알고리즘유형별/그리디/input.txt")

value = sys.stdin.readline()

#-- 0또는 1이 있으면 더하고 그게 아니면 곱함

plus = False
if int(value[0]) <= 1:
    plus = True
answer = int(value[0])

for i in range(1, len(value)):
    if plus == True:
        answer +=  int(value[i])
        if int(value[i]) <= 1:
            continue
        plus = False
    else:
        answer = answer * int(value[i])
print(answer)