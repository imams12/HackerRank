# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
a = OrderedDict()

for i in range(n):
  b = input().strip()
  if b in a:
    a[b] += 1
  else:
    a[b] = 1
    
print(len(a))
for key, value in a.items():
  print(value, end=' ')
