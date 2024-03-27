n = int(input())
arr = list(map(int, input().split()))
target = int(input())
j = 0
for i in range(n):
    if target == arr[i]:
        j += 1
print(j)