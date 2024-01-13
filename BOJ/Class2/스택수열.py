import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
targets = []
for _ in range(n):
    targets.append(int(sys.stdin.readline()))

stack = []
traces = []
value = 1
idx = 0

while n > idx:
    target = targets[idx]
    if len(stack) != 0 and target < stack[-1]:
        print("NO") #-- 오름차순이기 때문에 값이 더 크면 답 없음
        sys.exit()
    if len(stack) != 0 and target == stack[-1]:
        traces.append("-")
        stack.pop()
        idx+=1
        continue
    else:
        stack.append(value)
        value+=1
        traces.append("+")    
for trace in traces:
    print(trace)