# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
  a, b = map(str, input().split())
  try:
    print(int(a)//int(b))
  except ZeroDivisionError as c:
    print("Error Code:",c)
  except ValueError as d:
    print("Error Code:",d)
