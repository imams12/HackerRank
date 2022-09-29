# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
set_A = set(map(int, input().split()))
for i in range(int(input())):
  command, *k = map(str, input().split())
  set_B = set(map(int, input().split()))
  if command == "update":
    set_A.update(set_B)
  elif command == "intersection_update":
    set_A.intersection_update(set_B)
  elif command == "difference_update":
    set_A.difference_update(set_B)
  elif command == "symmetric_difference_update":
    set_A.symmetric_difference_update(set_B)

print(sum(set_A))
