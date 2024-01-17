import sys
import math
# MAX_N = 500000 #-- 100만
# print(MAX_N * math.log2(MAX_N)) 

# sys.stdin = open("input.txt")
dic = dict()
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for card in cards:
    if dic.get(card) == None: 
        dic[card] = 1
    else:
        dic[card] +=1

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    if target in dic:
        print(dic[target], end=" ")
    else:
        print(0, end=" ")