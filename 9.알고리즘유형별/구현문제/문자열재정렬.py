import sys
sys.stdin = open("9.알고리즘유형별/input.txt")

strings = sys.stdin.readline()
strings = sorted(strings, reverse=False)

total = 0
for string in strings:
    if string >='0' and string <='9':
        total += int(string)
        continue
    else:
        print(string, end='')
print(total)
