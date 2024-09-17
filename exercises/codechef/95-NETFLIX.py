# cook your dish here
n = int(input())
for _ in range(n):
    amounts = list(map(int, input().split()))
    cost = amounts[-1]
    amounts = amounts[:-1]
    print("YES" if any(a + b >= cost for i, a in enumerate(amounts) for b in amounts[i+1:]) else "NO")