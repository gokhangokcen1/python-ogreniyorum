#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
	if s[-2:] == "PM":
		if s[:2] != "12":
			return f"{int(s[:2])+12}{s[2:-2]}"
		else:
			return f"{s[:2]}{s[2:-2]}"
	else:
		if s[:2] == "12":
			return f"00{s[2:-2]}" 
		else:
			return s[:-2]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
