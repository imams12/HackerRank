# Solution 1
K = int(input()) 
room = list(map(int, input().split())) 
s = set(room) 
for element in list(s): 
    room.remove(element) 
s2 = set(room)
s = s.difference(s2) 
for element in s: 
    print(element)

# Solution 2
from collections import Counter

K = int(input())
room = map(int, input().split())
roomset = dict(Counter(room))
for key, value in roomset.items():
  if value == 1:
    print(key)
