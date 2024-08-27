# cook your dish here
c = int(input())

for i in range(c):
    a,b,c,d = map(int, input().split())
    
    print(a + (b - c)*d)