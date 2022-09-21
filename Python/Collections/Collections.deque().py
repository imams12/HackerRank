# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
d = deque()
for i in range(n):
  command, *k = input().split()
  if command == 'append':
    d.append(int(*k))
  elif command == 'appendleft':
    d.appendleft(int(*k))
  elif command == 'clear':
    d.clear()
  elif command == 'extend':
    d.extend(int(*k))
  elif command == 'count':
    d.count(int(*k))
  elif command == 'pop':
    d.pop()
  elif command == 'popleft':
    d.popleft()
  elif command == 'remove':
    d.remove(int(*k))
  elif command == 'reverse':
    d.reverse()
  
print(*d)
