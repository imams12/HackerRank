# A valid mobile number is a ten digit number starting with a 7, 8, or 9
import re

regex_pattern = r"^[789][0-9]{9}$"
for i in range(int(input())):
  print("YES") if bool(re.match(regex_pattern, input())) == True else print("NO")
