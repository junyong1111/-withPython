import sys
sys.stdin = open("9.알고리즘유형별/그리디/input.txt")

string = sys.stdin.readline()
one = 0
zero = 0
for s in string:
    if int(s) == 0:
        zero+=1
    else:
        one+=1
if one < zero:
    target = 0
else:
    target = 1

answer = 0 
length = 0

for i in range(len(string)):
    if int(string[i]) == target:
        if length == 0:
            continue
        else:
            answer +=1
            length = 0
    else:
        length+=1
print(answer)