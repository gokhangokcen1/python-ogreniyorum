# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print((x*3) if (x*3) < (y*2) else (y*2))