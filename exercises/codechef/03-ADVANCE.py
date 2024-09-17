# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if x <= y <= x+200:
        print("YES")
    else:
        print("NO")