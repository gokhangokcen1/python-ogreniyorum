# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())

def is_prime(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    
    return True
    
for i in range(n):
    number = int(input())
    
    if is_prime(number):
        print("Prime")
    else:
        print("Not prime")

