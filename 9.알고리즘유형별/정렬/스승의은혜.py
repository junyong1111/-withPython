import sys
sys.stdin = open("9.알고리즘유형별/input.txt")

students, balance = map(int, sys.stdin.readline().split())
gifts = []

for _ in range(students):
    gifts.append(list(map(int, sys.stdin.readline().split())))

gifts = sorted(gifts, key=lambda gift : gift[0]+gift[1])
answer = 0
for i in range(students):
    current_balance = balance
    if current_balance < (gifts[i][0]//2) + gifts[i][1]:
        break
    gitf = 1
    current_balance -= (gifts[i][0]//2) + gifts[i][1]
    
    for j in range(students):
        if i==j:
            continue
        price, delivery = gifts[j]
        if current_balance >= price+delivery:
            gitf+=1
            current_balance -= price+delivery
    answer = max(answer, gitf)
    
print(answer)