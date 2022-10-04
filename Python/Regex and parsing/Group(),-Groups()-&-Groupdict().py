# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

match = re.search(r"([a-zA-Z0-9])\1+", input())
print(match.group()[0] if match else -1)
