# cook your dish here
c = int(input())

for i in range(c):
    w,x,y,z = map(int, input().split())
    left = x - w
    flow = y * z
    if left > flow:
        print("Unfilled")
    elif left == flow:
        print("filled")
    else:
        print("overflow")
    