# cook your dish here
c = int(input())

def secondMax(x,y,z):
    if (x > y and x < z) or (x > z and x < y): 
        return x
    elif (y > x and y < z) or (y > z and y < x):
        return y
    elif (z > x and z < y) or (z > y and z < x):
        return z

    
for i in range(c):
    x,y,z = map(int, input().split())
    print(secondMax(x,y,z))

