import sys
# sys.stdin = open("BOJ/Class2/input.txt")

numbers = list(map(int, sys.stdin.readline().split()))

def swap(a, b):
    temp = a%b
    a = b
    b = temp
    return a, b

def gcd(a, b):
    while b:
        a,b = swap(a,b)
    return a
    
def lcd(a, b):
    return a*b//gcd(a,b)
 # a와 b의 곱을 a와 b의 최대공약수로 나누어 최소공배수 구함

print(gcd(numbers[0], numbers[1]))
print(lcd(numbers[0], numbers[1]))