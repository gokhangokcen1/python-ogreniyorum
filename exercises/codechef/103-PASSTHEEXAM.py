# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    print("PASS" if (x >= 10 and y >= 10 and z >= 10) and (x+y+z >= 100) else "FAIL")