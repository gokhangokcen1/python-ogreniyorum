# cook your dish here
for _ in range(int(input())):
    input()
    L1 = list(map(int, input().split()))
    c = 0
    for i in L1:
        if i >= 1000:
            c += 1

    print(c)
        