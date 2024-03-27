import sys

arr =[]
while(True):
    a, b = map(int, sys.stdin.readline().split())
    if(a==b==0):
        break
    arr.append(a+b)
for i in arr:
    print(i)