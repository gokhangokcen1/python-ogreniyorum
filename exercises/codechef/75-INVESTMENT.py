# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print("YES" if 2*y <= x else "NO")