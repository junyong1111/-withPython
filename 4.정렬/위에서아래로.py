import sys
sys.stdin = open("4.정렬/input.txt")

#-- 내림차순 정렬
n = sys.stdin.readline()

arr = []
for i in range(3):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr, reverse=True)
for data in arr:
    print(data, end=' ')
print()