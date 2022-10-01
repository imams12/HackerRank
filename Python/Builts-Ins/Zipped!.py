# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X =map(int, input().split())
Total = []
for i in range (X):
  subject = tuple(map(float, input().split()))
  Total.append(subject)
  
for i in zip(*Total):
  print(sum(i) / X)
