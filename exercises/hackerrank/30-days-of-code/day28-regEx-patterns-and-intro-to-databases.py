#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    arr = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        
        
        if emailID.split("@")[1] == "gmail.com":
            arr.append(firstName)
        else:
            continue

    for i in range(len(arr)):

        print(sorted(arr)[i])
        
