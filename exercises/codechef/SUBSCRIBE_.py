# cook your dish here
c = int(input())

for i in range(c):
    x,y = map(int, input().split())
    subscriptions_needed = (x + 5) // 6

    total_cost = subscriptions_needed * y
    

    print(total_cost)
