# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s, k = input(), input()
if re.search(r""+k+"", s):
    for m in re.finditer(r"(?=("+k+"))", s):
        print(f"({m.start(1)}, {m.end(1)-1})")
else:
    print("(-1, -1)")
