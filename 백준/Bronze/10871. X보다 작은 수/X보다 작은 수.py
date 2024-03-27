n,target = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in range(n):
    if target > arr[i]:
        result.append(arr[i])
for i in result:
    print(i,end = ' ')