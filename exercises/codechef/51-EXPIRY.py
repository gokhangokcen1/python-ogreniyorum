# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    if y * z >= x:
        print("Yes")
    else:
        print("No")