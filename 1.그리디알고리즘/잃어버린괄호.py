import sys
import re
# sys.stdin = open('1.그리디알고리즘/input.txt')

data = sys.stdin.readline()
numbers = re.findall(r'\d+', data)
intList = list(map(int, numbers))

cal = []
for i in range(len(data)):
    if data[i] == '-' or data[i] == '+':
        cal.append(data[i])

if len(cal) != 0:
    if cal[0] == '-':
        flag = True
    else :
        flag = False
        
    for i in range(1, len(cal)):
        if cal[i] == '+':
            if flag == True:
                cal[i] = '-'
        else:
            flag = True

    answer = 0
    for i in range(len(cal)):
        if cal[i] == '-':
            intList[i+1] = intList[i] - intList[i+1]
        else:
            intList[i+1] = intList[i] + intList[i+1]

print(intList[-1])
    