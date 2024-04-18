import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())

numbers = [i for i in range(1, N+1)]
start = 0

answer = []
while numbers:
    index = (start+K-1) % len(numbers)
    answer.append(numbers[index])
    del numbers[index]
    start = index

print("<", end="")
for i in range(len(answer)):
    if (i+1) == len(answer):
        break
    else:
        print(answer[i], end=", ")
print("{}>".format(answer[-1]))

        
    

    
    
    
    
    

           