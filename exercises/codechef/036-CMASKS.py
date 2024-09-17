# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    cloth = x * 100
    masks = y * 10
    if cloth >= masks:
        print("Cloth")
    else:
        print("Disposable")