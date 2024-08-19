# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    print(4 * x + 2 * y + 0 * z)