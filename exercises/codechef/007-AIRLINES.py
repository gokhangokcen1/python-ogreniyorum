# cook your dish here
c = int(input())

for i in range(c):
    x,y,z = map(int, input().split())
    seats = 10 * x
    if y >= seats:
        print(seats * z)
    else:
        print(y * z)