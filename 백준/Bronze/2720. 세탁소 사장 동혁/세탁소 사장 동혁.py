num = int(input())
q = 25
d = 10
n = 5
p = 1

for i in range(num):
    gold = int(input())
    print(gold//q,end=' ')
    gold -= (gold//q)*q
    print(gold // d, end=' ')
    gold -= (gold//d)*d
    print(gold // n, end=' ')
    gold -= (gold // n) * n
    print(gold // p, end=' ')
    gold -= (gold // p) * p
    print()