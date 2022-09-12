# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()
hasil = list(permutations(s,int(k)))
hasil_s = sorted(hasil)

for i in hasil_s:
  print(''.join(i))
