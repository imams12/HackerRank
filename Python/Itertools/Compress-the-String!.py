# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1
from itertools import groupby

s = input()
for key, group in groupby(s):
  print((len(list(group)), int(key)), sep='', end=' ')

# Solution 2
from itertools import groupby

s = input()
hasil = [str((len(list(g)), int(k))) for k,g in groupby(s)]
print(*hasil)
