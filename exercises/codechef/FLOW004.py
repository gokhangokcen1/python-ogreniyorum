# cook your dish here
c = int(input())

for i in range(c):
    n = input()
    l = [int(i) for i in n]
    print(l[0] + l[-1])
    