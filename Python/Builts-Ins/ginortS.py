# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
lower = []
upper = []
odd = []
even = []
for i in range(len(S)):
  if S[i].islower():
    lower.append(S[i])
  elif S[i].isupper():
    upper.append(S[i])
  elif S[i].isdigit() and int(S[i]) % 2 == 1:
    odd.append(S[i])
  else:
    even.append(S[i])
    
lower_sort = sorted(lower)
upper_sort = sorted(upper)
odd = sorted(odd)
even = sorted(even)
print(''.join(lower_sort) + ''.join(upper_sort) + ''.join(odd) +  ''.join(even))
