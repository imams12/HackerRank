# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()
hasil = list(combinations_with_replacement(sorted(s.upper()), int(k)))
for i in hasil:
  print(*i, sep='')
