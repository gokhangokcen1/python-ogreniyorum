# cook your dish here
c = int(input())

for i in range(c):
    n = int(input())
    if n <= 70:
        print(0)
    elif n > 70 and n <= 100:
        print(500)
    else:
        print(2000)