import sys
sys.stdin = open("input.txt")

testcase =  int(input())
number = 1  
while testcase:
    testcase-=1
    N = int(input())
    
    prices = list(map(int, input().split()))[::-1]
    answer = maxvalue = 0
    
    for n in prices:
        if maxvalue < n:
            maxvalue = n
        else:
            answer += maxvalue - n    
            
    print("#{} {}".format(number, answer))
    number+=1