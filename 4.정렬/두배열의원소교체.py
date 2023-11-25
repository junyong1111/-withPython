import sys
sys.stdin = open("4.정렬/input.txt")

'''
K 번 바꿔치기 해서 
A 배열의 합이 최대가 되도록 해야 한다
A 오름차순 정렬
B 내림차순 정렬
K만큼 앞에서부터 swap
'''

n,k = map(int, sys.stdin.readline().split())
# print(n, k)

arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

arrA = sorted(arrA, reverse = False)
arrB = sorted(arrB, reverse = True)

for i in range(k):
    if arrA[i]< arrB[i]:
        arrA[i] = arrB[i]
print(sum(arrA))