# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print(10 * x + 90 * y)