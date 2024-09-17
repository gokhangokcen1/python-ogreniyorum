# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    print(int((z-y)/x))