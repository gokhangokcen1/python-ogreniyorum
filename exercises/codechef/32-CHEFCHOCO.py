# cook your dish here
n = int(input())

for _ in range(n):
    amounts = list(map(int, input().split()))
    cost = amounts[-1]
    amounts = amounts[:-1]
    
    found = False
    for i in range(len(amounts)):
        for j in range(i + 1, len(amounts)):
            if amounts[i] + amounts[j] >= cost:
                found = True
                break
        if found:
            break

    print("YES" if found else "NO")