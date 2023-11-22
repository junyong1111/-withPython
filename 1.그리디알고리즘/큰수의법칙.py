import sys

sys.stdin = open('input.txt')

N, M, K = map(int, sys.stdin.readline().split())

arr = (list(map(int, sys.stdin.readline().split())))
#2 4 5 4 6
arr.sort(reverse=True)
answer = 0
cnt = M
flag = True

while cnt > 0:
    if flag == True:
        if cnt - K >= 0:
            answer += arr[0] * K
            flag = False
            cnt = cnt - K
        else :
            answer += arr[0] * cnt
            break
    else:
        answer += arr[1]
        cnt = cnt -1
        flag = True
            
        
print(answer)
    