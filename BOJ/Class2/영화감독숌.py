import sys
# sys.stdin = open("BOJ/Class2/input.txt")
n = int(sys.stdin.readline())

title = "666"
value = 0
cnt = 0 
while True:
    if title in str(value):
        cnt +=1
        if cnt == n:
            print(value)
            break
    value+=1