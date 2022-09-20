# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()
for i in range(1,int(k)+1):
  hasil = list(combinations(sorted(s.upper()),i))
  for i in hasil:
    print(*i, sep='')
