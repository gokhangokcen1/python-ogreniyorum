# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print("YES" if y >= (x*3) else "NO")