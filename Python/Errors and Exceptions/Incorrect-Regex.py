# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
  try:
    re.compile(input())
    print(True)
  except re.error:
    print(False)
