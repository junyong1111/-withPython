import sys
import re
# sys.stdin = open("BOJ/Class3/input.txt")

exp = sys.stdin.readline()
numbers = re.findall(r'\d+', exp)
numbers = list(map(int, numbers))            

cal = []
for i in range(len(exp)):
    if exp[i] == '-' or exp[i] == '+':
        cal.append(exp[i])

if len(cal) == 0:
    print(numbers[-1])
    sys.exit()

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
        numbers[i+1] = numbers[i] - numbers[i+1]
    else:
        numbers[i+1] = numbers[i] + numbers[i+1]

print(numbers[-1])
