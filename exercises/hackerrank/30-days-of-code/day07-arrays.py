import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    print(*arr[::-1])


    # for döngüsü ile 
    # for i in range(len(arr)-1, -1, -1):
    #     print(arr[i], end=" ")