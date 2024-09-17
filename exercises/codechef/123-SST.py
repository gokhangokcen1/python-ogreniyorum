# cook your dish here
for _ in range(int(input())):
    x,y = map(int, input().split())
    if x > y / 2:
        print("FIRST")
    elif x < y / 2:
        print("SECOND")
    else:
        print("ANY")