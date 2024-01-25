import sys
# sys.stdin = open("BOJ/Class2/input.txt")

def isPalindrome(word):
    start = 0
    end = len(word)-1
    while start<end:
        if word[start] == word[end]:
            start +=1
            end-=1
        else:
            return False
    return True
            
while True:
    word = sys.stdin.readline().strip()
    if word == "0":
        break   
    if isPalindrome(word):
        print("yes")
    else:
        print("no")