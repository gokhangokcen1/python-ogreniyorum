# cook your dish here
c = int(input())

for i in range(c):
    a,b,c = map(int, input().split())
    average = (a+b)/2
    print("YES" if average > c else "NO")