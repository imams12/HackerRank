# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())
for i in range(T):
  num_cube = int(input())
  deq_elemen = deque(list(map(int, input().split())))
  temp_elemen = max(deq_elemen)
  Answer ="Yes"
  for j in range(num_cube):
    if deq_elemen[0] <= deq_elemen[-1]:
      max_elemen = deq_elemen[-1]
      deq_elemen.pop()
    else:
      max_elemen = deq_elemen[0]
      deq_elemen.popleft()
    if temp_elemen >= max_elemen:
      temp_elemen = max_elemen
    else:
      Answer = "No"
      break 
    
  print(Answer)
