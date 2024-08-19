# cook your dish here
c = int(input())

for i in range(c):
    n = int(input())
    if n < 3: 
        print("LIGHT")
    elif n >= 7:
        print("HEAVY")
    else:
        print("MODERATE")

        