#-- 최대 N
import sys
# sys.stdin = open("BOJ/Class2/input.txt")

def balanceWorld(string):
    index = 0
    stack = []
    while string[index] != ".":
        char = string[index]
        if char == "(":
            stack.append(char)
        elif char == "[":
            stack.append(char)
        elif char == ")" :
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()
        elif char == "]" :
            if len(stack) == 0 or stack[-1] != "[":
                return False
            else:
                stack.pop()
        index +=1
    if len(stack) == 0:
        return True
    return False
        
        
while True:
    string = sys.stdin.readline().rstrip()
    if string[0] == '.' and len(string) == 1:
        break
    if balanceWorld(string):
        print("yes")
    else:
        print("no")