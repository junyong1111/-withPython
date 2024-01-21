import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
answer = [i for i in range(500)]
print(answer[(n//5) + (n//25)+ (n//125)])


"""
1~4 = 0
5~9 = 1
10~14 = 2
15~19 = 3

20 ~ 24 = 4
25 ~ 29 = 6

30 ~ 34 = 7
35 ~ 39 = 8

40 ~ 44 =9
45 ~ 49 = 10

50 ~ 54 = 12
55 ~ 59 = 13

60 ~ 64 = 14
65 ~ 69 = 15

70 ~ 74 = 16
75 ~ 79 = 18
"""    