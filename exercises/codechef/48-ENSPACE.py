# cook your dish here
c = int(input())

for i in range(c):
    n,x,y = map(int, input().split())
    print("YES" if n >= (x + 2 * y) else "NO")