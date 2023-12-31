import sys
# sys.stdin = open("input.txt")/

#-- 생성자는 더 작을 수 밖에 없음
n = int(sys.stdin.readline())
def findvalue(number):
    ret = number
    while number:
        ret += number % 10
        number = number//10
    return ret

flag = False
ret = 0
for i in range(1, n+1): 
    if findvalue(i) == n:
        flag = True
        ret = i
        break
if flag :
    print(ret) #-- 생성자가 있는 경우
else: 
    print(0) #-- 생성자가 없는 경우
# 2~3중 반복문 가능