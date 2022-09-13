# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
l = defaultdict(list)
for i in range(n):
  l[input()].append(i+1)
for j in range(m):
  t = input()
  if (len(l[t])) == 0:
    print(-1)
  else:
    print(*l[t])
