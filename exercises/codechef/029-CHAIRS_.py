# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if x >= y:
        print(x-y)
    elif y == 0:
        print(x)
    else:
        print(0)
        