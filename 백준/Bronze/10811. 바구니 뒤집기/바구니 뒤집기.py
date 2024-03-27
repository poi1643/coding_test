import sys
a,b = map(int, sys.stdin.readline().split())
arr = list(range(1,a+1))
for i in range(b):
    c,d = map(int, input().split())
    arr[c-1:d] = arr[c-1:d][::-1]

print(* arr)