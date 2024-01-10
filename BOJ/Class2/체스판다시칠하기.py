import sys
# sys.stdin = open("BOJ/Class2/input.txt")

def myprint(board, n, m):
    for i in range(n):
        for j in range(m):
            print(board[i][j], end=' ')
        print()    
MAX_SIZE = 8
n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    data = sys.stdin.readline().split()
    for j in range(m):
        board[i][j] = data[0][j]

# myprint(board, n, m)    
def cut8x8(board, x, y):
    cut_board = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            cut_board[i][j] = board[i+y][j+x]
    return cut_board

def chageColor(color):
    if color == "B":
        return "W"
    return "B"

def reverseBoard(cut_board, arg):
    cnt = 0
    if arg == "Black":
        color = "B"
    else:
        color = "W"
    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            if cut_board[i][j] == color:
                color = chageColor(color)
                continue
            else:
                cut_board[i][j] = color
                color = chageColor(color)
                cnt = cnt+1
        color = chageColor(color)
    return cnt 

answer = (MAX_SIZE*MAX_SIZE)+1
for i in range(0, (n-MAX_SIZE)+1):
    for j in range((m-MAX_SIZE)+1):
        #-- step1. 2개의 8x8 자르기
        cut_board_black = cut8x8(board, j, i)
        cut_board_white = cut8x8(board, j, i)
        #-- step2. 체스판 뒤집기
        #-- 2-1 Black
        answer = min(reverseBoard(cut_board_black, "Black"), answer)
        #-- 2-2 White
        answer = min(reverseBoard(cut_board_white, "White"), answer) 
print(answer)        