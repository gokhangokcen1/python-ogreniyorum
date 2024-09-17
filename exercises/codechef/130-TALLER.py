# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    print("A" if x > y else "B")
            