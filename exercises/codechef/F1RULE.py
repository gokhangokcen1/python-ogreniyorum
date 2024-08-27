# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print("YES" if (x*1.07)>=y else "NO")