# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    new_selling = x * 1.1 
    z = x-y 
    print(int(new_selling-z))