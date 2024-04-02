import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

#-- step1. 중복 제거 후 정렬 
copy_numbers = list(set(numbers))
copy_numbers.sort()

#-- step2. 각각 좌표를 인덱스에 맞게 매핑
mydict = dict()
for i in range(len(copy_numbers)):
    mydict[copy_numbers[i]] = i

#-- step3. 각각 좌표를 Key 인덱스를 Value로 출력
for number in numbers:
    print(mydict[number], end=" ")
print()