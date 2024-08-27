# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if x < y:
        print(0)
    else:
        print(int(x/(y*3)))