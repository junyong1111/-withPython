import sys
sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline
N, L = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    
def myprint():
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()
myprint()


while True:
    
    
    
    
    
        
        
        
    