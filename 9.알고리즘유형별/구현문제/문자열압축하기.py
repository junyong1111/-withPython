import sys
sys.stdin = open("9.알고리즘유형별/input.txt")
s = sys.stdin.readline()

answer = len(s)
for i in range(1, (len(s)//2) +1): #-- 몇 개로 나눌지 
    pos = 0 #-- 왼쪽부터 시작
    length = len(s)
    # aabbaccc
    while pos + i <= len(s):
        target = s[pos:pos+i] # a
        pos+=i #- 시작 + 나눈 단어의 개수만큼 전진
        cnt = 0
        while pos+i <= len(s):
            if target == s[pos:pos+i]: #-- 중복단어가 있다면
                cnt+=1
                pos+=i
            else: #-- 없다면 종료
                break
            
        # print("target is {}, duplicate is {}".format( target, cnt))
        if cnt > 0:
            length -= i*cnt
            if cnt < 9:
                length +=1
            elif cnt <99:
                length +=2
            elif cnt <999:
                length +=3
            else:
                length +=4
    answer = min(answer, length)
print(answer)            
            
            
        
