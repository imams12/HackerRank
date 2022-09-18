# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happines = 0
for i in arr:
  if i in A:
    happines += 1
  elif i in B:
    happines -= 1
print(happines)
