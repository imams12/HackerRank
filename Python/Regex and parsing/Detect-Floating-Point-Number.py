# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
for i in range(T):
  N = input()
  if re.search(r'^[-+]?\d*\.\d*$',N):
    print(True)
  else:
    print(False)
