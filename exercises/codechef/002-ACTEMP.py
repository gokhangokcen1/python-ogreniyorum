# cook your dish here
for _ in range(int(input())):
    x,y,z = map(int, input().split())
    if y >= x and z<=y:
        print("Yes")
    else:
        print("No")
    