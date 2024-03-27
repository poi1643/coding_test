import sys
a,b = map(int, sys.stdin.readline().split())
arr = list(range(1,a+1))
for i in range(b):
    c, d = map(int, sys.stdin.readline().split())
    c = c-1
    d = d-1
    temp = arr[c]
    arr[c] = arr[d]
    arr[d] = temp

print(* arr)