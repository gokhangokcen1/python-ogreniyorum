# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    if 2 * x > 5 * y:
        print("Chocolate")
    elif 2 * x == 5 * y:
        print("Either")
    else:
        print("Candy")