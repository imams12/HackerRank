import re

for i in range(int(input())):
  card_number = input().strip()
  card_number_removed_hypen = card_number.replace("-","")
  
  valid = True
  
  length_16 = bool(re.match(r"^[4-6]\d{15}$", card_number))
  length_19 = bool(re.match(r"^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$", card_number))
  consecutive = bool(re.findall(r"(?=(\d)\1\1\1)", card_number_removed_hypen))
  
  if length_16 == True or length_19 == True:
    if consecutive == True:
      valid = False
  else:
    valid = False
  if valid == True:
    print("Valid")
  else:
    print("Invalid")
