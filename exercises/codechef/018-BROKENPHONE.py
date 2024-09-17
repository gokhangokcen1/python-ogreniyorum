# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if x<y:
        print("REPAIR")
    elif x>y:
        print("NEW PHONE")
    else:
        print("ANY")