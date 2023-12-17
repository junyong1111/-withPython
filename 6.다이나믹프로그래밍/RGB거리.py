import sys
sys.stdin = open("6.다이나믹프로그래밍/input.txt")

houses = int(sys.stdin.readline())
rgb = [[0 for _ in range(3)] for _ in range(houses)]

for i in range(houses):
    data = sys.stdin.readline().split()
    for j in range(3):
        rgb[i][j] = int(data[j])

# for i in range(houses):
#     for j in range(3):
#         print(rgb[i][j], end= " ")
#     print()

dp = [0] * (houses+1)

    
    


    
    


