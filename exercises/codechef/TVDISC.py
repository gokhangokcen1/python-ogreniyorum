# cook your dish here
c = int(input())

for i in range(c):
    x,y,z,t = map(int, input().split())
    if (x-z) < (y-t):
        print("First")
    elif (x-z) > (y-t):
        print("Second")
    else:
        print("Any")