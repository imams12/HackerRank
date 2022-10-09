# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

x = int(input())
N = [input().strip() for i in range(x)]
regex_pattern = "\{[^\{\}]+\}"
regex_pattern1 = r"\#[0-9A-Fa-f]{6}|\#[0-9A-Fa-f]{3}"
m = re.findall(regex_pattern, "'" + ("".join(N)) + "'")
for i in m:
  l = re.findall(regex_pattern1, i)
  if len(l) > 0:
    print(*l, sep='\n')
  else:
    continue
