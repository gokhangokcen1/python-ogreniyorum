# cook your dish here
for _ in range(int(input())):
    x,y = map(int, input().split())
    c,d = map(int, input().split())
    
    if x > c or y > d:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")