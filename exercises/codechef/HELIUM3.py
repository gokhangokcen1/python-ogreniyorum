# cook your dish here
for _ in range(int(input())):
    a,b,x,y = map(int, input().split())
    print("Yes" if (x*y) >= (a*b) else "No")