# cook your dish here
c = int(input())

for i in range(c):
    n = int(input())
    first = n * 0.1 
    if first > 100:
        print(int(first))
    else:
        print(100)