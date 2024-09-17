# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print("YES" if (x+y) % 2 == 0 else "NO")