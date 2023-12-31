import sys
# sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
strings = []
for _ in range(n):
    strings.append(sys.stdin.readline().strip())

uniqueStrings = list(set(strings))
uniqueStrings = sorted(uniqueStrings, key=lambda str : str)
result = sorted(uniqueStrings, key=lambda str : len(str))

for ret in result:
    print(ret)