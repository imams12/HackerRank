# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", input())
print(-1) if S == [] else print(*S, sep="\n")
