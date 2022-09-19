# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
item_dictionary = OrderedDict()
for i in range(n):
  *key, value = input().split()
  key = " ".join(key)
  if key in item_dictionary:
    item_dictionary[key] += int(value)
  else:
    item_dictionary[key] = int(value)
for key,value in item_dictionary.items():
    print(key,value)
