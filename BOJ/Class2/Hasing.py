import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
string = sys.stdin.readline()

total = 0
r = 31
M = 1234567891
for i in range(n):
    hash_value = ord(string[i]) - 96
    total += ((hash_value * (r**i))) %M
print(total%M)