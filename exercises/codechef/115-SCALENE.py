t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    t -= 1
    if (a != b and a != c) and b != c:
        print("YES")
    else:
        print("NO")
