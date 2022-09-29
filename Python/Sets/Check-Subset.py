# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
  a = int(input())
  set_a = set(map(int, input().split()))
  b = int(input())
  set_b = set(map(int, input().split()))
  if set_a.intersection(set_b) == set_a:
    print(True)
  else:
    print(False)
