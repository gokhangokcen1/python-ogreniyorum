# cook your dish here
c = int(input())

for i in range(c):
    following,follower = map(int, input().split())
    print("YES" if following > follower * 10 else "NO")