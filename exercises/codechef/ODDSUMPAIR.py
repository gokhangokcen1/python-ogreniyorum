# cook your dish here
c = int(input())

for i in range(c):
    numbers = list(map(int, input().split()))
    
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    even_count = len(numbers) - odd_count
    
    if odd_count > 0 and even_count > 0:
        print("YES")
    else:
        print("NO")