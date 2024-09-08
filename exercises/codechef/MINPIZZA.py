# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    print(int((x*y)/4) if ((x*y) % 4 == 0) else int((x*y)/4)+1)