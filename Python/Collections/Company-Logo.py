#!/bin/python3
from collections import Counter

print(*[f"{x} {y}" for x, y in Counter(sorted(input())).most_common(3)], sep='\n')
