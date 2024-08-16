t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())
    # write your code here
    result = "YES" if (x+y) > 6 else "NO" 
    print(result)