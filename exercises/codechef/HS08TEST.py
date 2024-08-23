# cook your dish here
x,y = map(float, input().split())

if y >= x + 0.5:
    if x % 5 == 0:
        result = y - x - 0.5
        print(f"{result:.2f}")
    else:
        print(f"{y:.2f}")
else:
    print(f"{y:.2f}")