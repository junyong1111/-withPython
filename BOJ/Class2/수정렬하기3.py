import sys
# sys.stdin = open("BOJ/Class2/input.txt")
MAX_SIZE =10001
n = int(sys.stdin.readline())
counting = [0] * MAX_SIZE #-- 계수정렬 배열 생성
for _ in range(n):
    counting[int(sys.stdin.readline())] +=1 #-- 해당 인덱스 +1

for i in range(MAX_SIZE):
    if counting[i] !=0 :
        while counting[i]: #-- 남은거 털어내기 
            print(i)
            counting[i]-=1