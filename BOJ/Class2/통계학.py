#-- 최대 NlongN
import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
MAX_SIZE = 8000 #-- -4000 ~ 4000
values = [0] * (MAX_SIZE+2)
arr = []
total = 0
for _ in range(n):
    value = int(sys.stdin.readline())
    arr.append(value)
    if value < 0:
        value = (value *-1) + MAX_SIZE//2
    values[value] += 1

def Count(): #-- 최대 빈도 수 계산
    cnt = 0
    for i in range(len(values)):
        if cnt < values[i]:
            cnt = values[i]
    return cnt

def mode(): #-- 최빈값이 여러개의 경우를 확인하기 위헤
    cnt = Count()
    answer = []
    for i in range(len(values)):
        index = i
        if cnt == values[i]:
            if i > 4000:
                index = (i-(MAX_SIZE//2)) *-1
            answer.append(index)
    answer.sort()
    if len(answer) == 1:
        return answer[0]
    else:
        return answer[1]
    # 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    


#-- 산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum(arr)/len(arr)))

#-- 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
median = sorted(arr)
print(median[len(median)//2])

#-- 최빈값 : N개의 수들 중 가장 많이 나타나는 값
print(mode())

#-- 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(arr) - min(arr))