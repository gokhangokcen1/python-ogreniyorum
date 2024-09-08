# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    print("OUT" if a+b+c+d >= 1 else "IN")