# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex_pattern = r"^<[a-z][\w\-\.]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>$"
for i in range(int(input())):
  name, email = list(map(str, input().split()))
  if bool(re.search(regex_pattern, email)) == True:
    print(name, email)
