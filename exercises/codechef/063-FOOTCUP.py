# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    
    if (x != 0 and y != 0):
        if (x == y):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        