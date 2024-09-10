# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if int(x%3) == 0:
        print(0)
    elif int(x%3) == 1:
        print(2)
    else:
        print(1)