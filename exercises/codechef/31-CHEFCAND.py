# cook your dish here
import math
for _ in range(int(input())):
    x,y = map(int, input().split())
    if y > x:
        print(0)
    else:
        print(int(math.ceil((x-y)/4)))
    