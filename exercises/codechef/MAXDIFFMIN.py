# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    print(max(x,y,z) - min(x,y,z))
    