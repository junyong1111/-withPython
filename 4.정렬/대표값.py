arr = [0 for _ in range(5)]
for i in range(5):
    arr[i] = int(input())

arr = sorted(arr)
print(sum(arr)//5)
print(arr[2])