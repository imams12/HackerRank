import re

UIDS = []
for i in range(int(input())):
  UID = input()
  UIDS.append(UID)
  
for UID in UIDS:
  if not re.fullmatch(r"[a-zA-Z0-9]{10}", UID):
    print("Invalid")
  elif not len(re.findall(r"[A-Z]", UID)) >= 2:
    print("Invalid")
  elif not len(re.findall(r"[0-9]", UID)) >= 3:
    print("Invalid")
  elif re.search(r"([a-zA-Z0-9]).*\1", UID):
    print("Invalid")
  else:
    print("Valid")
