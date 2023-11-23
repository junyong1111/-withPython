import sys
import pprint

sys.stdin = open('2.구현/input.txt')
n = int(sys.stdin.readline())


'''
#-- 1이 입력된 경우
00시 00분 00초 ~ 01시 59분 59초 까지 3이 포함된 경우의 수
00시 00분 03초
00시 00분 33초
00시 03분 00초
00시 03분 03초
....
'''

hours = n
mins = 60
secs = 60

cnt = 0
for hour in range(hours+1): #-- 시간을 포함해야 함
    for m in range(mins):
        for sec in range(secs):
            if '3' in str(sec) + str(m) + str(hour) :
                cnt +=1
print(cnt)