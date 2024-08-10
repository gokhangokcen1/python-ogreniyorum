#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    dec_to_bin = bin(n)[2:]

    left = 0
    right = 0

    for i in dec_to_bin:
        if i != '0':
            left +=1 
        else:
            break

    for j in dec_to_bin[::-1]:
        if j != '0':
            right += 1
        else:
            break

    print(max(left,right))