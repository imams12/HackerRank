## Solution 1
x = int(input())
N = list(map(int, input().split()))
y = int(input())
Total = []
for i in range(y):
  n, fee = map(int, input().split())
  if n in N:
    N.remove(n)
    Total.append(fee)
print(sum(Total))

## Solution 2
from collections import Counter
X = input()
x = input().split()
d = dict(Counter(x))
s = 0
for i in range(int(input())):
    key, value = input().split()
    if key in x and d[key] > 0:
        s += int(value)
        d[key] -= 1
print(s)
