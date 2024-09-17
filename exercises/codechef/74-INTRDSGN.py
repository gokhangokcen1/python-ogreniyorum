# cook your dish here
c = int(input())

for i in range(c):
    x,y,z,t = map(int, input().split())
    print(min(x+y, z+t))