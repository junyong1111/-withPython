import sys
import math
# sys.stdin = open("BOJ/Class2/input.txt")

def round(n):
    if n - int(n) >= 0.5:
        return math.ceil(n)
    else:
        return int(n)
    
n = int(sys.stdin.readline())
if n==0:
    print(0)
    sys.exit()
levles = []
for i in range(n):
    levles.append(int(sys.stdin.readline()))

top = round((n*0.15) )
bottom = round((n*0.15))

levles.sort()
answer = levles[bottom:(n-top)]
print(round((sum(answer)/(n-(top+bottom)))))