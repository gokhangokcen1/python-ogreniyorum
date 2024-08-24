# cook your dish here
a,b,c,d = map(int, input().split())

t = sum(1 for x in (a, b, c, d) if x >= 10)
    
print(t)