# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    
    if (x + y) < z or (x + z) < y or (z + y ) < x:
        print("Yes")
    else:
        print("No")