# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if x < y:
        print("FIRST")
    elif x == y:
        print("ANY")
    else:
        print("SECOND")