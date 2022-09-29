# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())
list_s = []
for i in range(K):
  b, *list_b = map(int, input().split())
  list_s.append(list_b)

Hasil = list(product(*list_s))
S = 0
A = []
for i in Hasil:
  for j in i:
    S += j**2
  A.append((S%M))
  S = 0
  
print(max(A))
