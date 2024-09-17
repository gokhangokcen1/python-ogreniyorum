# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print(0 if x > y else abs(x-y))
