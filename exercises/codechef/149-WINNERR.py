# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    P = max(a, b)
    Q = max(c, d)
    
    if P < Q:
        print("P")
    elif P > Q:
        print("Q")
    else:
        print("TIE")
