# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
  s = input()
  s1 = re.sub(r"(?<= )(&&)(?= )", "and", s)
  s2 = re.sub(r"(?<= )(\|\|)(?= )", "or", s1)
  print(s2)
