import sys
sys.stdin = open("BOJ/Class3/input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
numberToname = dict()
nameTonumber = dict()

for i in range(1, N+1):
    # -- Key : 문자, Value : 숫자
    # -- Key : 숫자, Value : 문자
    name = input().rstrip()
    print(name)
    if name not in nameTonumber:
        numberToname[i] = name
        nameTonumber[name] = i

answer = []

for _ in range(M):
    data = input().rstrip()
    try:
        number = int(data)
        if number in numberToname:
            answer.append(numberToname[number])
    except:
        name = data
        if name in nameTonumber:
            answer.append(nameTonumber[name])

for ans in answer:
    print(ans)