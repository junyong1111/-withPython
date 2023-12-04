import sys
# sys.stdin = open("5.이진탐색/input.txt")

number_of_house, routers = map(int, sys.stdin.readline().split())

houses = []
for _ in range(number_of_house):
    houses.append(int(sys.stdin.readline()))
houses.sort()

left = 0
right = max(houses)

while left < right:
    mid = (left + right) // 2 + 1
    total = 1
    router = houses[0]  #-- 가장 앞에 있는 집에 공유기 설치
    for i in range(1, len(houses)):
        distance = abs(router - houses[i]) #-- 설치한 공유기부터 거리 계산
        if distance >= mid: #-- 만약에 해당 위치에 공유기를 설치할 수 있으면
            router = houses[i] #-- 공유기 위치 변경
            total+=1
    if total < routers :#-- 공유기 개수보다 작으면 거리가 너무 멀다. 줄여야 함
        right = mid -1
    else: #-- 거리가 충분한 경우
        left = mid
print(left)  