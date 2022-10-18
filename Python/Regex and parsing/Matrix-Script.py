#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
mapping = ['' for _ in range(m)]
for row in matrix:
    for i, char in enumerate(row):
        mapping[i] += char
string = ''
for m in mapping:
    string += ''.join(m)
print(re.sub('(?<=[\d\w])[^\d\w]+(?=[\d\w])', ' ', string))
