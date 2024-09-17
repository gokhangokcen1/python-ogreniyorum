# cook your dish here
c = int(input())
for i in range(c):
    n = int(input())
    if n >= 4 and n < 7:
        print("MEDIUM")
    elif n < 4:
        print("MILD")
    else:
        print("HOT")