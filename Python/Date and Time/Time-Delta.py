#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
  fmt = '%a %d %b %Y %H:%M:%S %z'
  t1_dt = dt.strptime(t1, fmt)
  t2_dt = dt.strptime(t2, fmt)
  
  if (t1_dt.year + t2_dt.year) <= 6000:
    return str(abs(int((t1_dt - t2_dt).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
