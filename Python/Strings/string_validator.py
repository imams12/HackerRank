## Solution 1
if __name__ == '__main__':
    s = input()
    methods = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']

    flag = False
    for method in methods:
      for i in s:
        if getattr(i, method)() == True:
          flag = True
      print(flag)
      flag = False
      
## Solution 2
if __name__ == '__main__':
    s = input()
    flag = any(map(str.isalnum, s))
    print(flag)
    truth = map(str.isalpha, s)
    print(any(truth))
    truth = map(str.isdigit, s)
    print(any(truth))
    if flag:
        truth = map(str.islower, s)
        print(any(truth))
        truth = map(str.isupper, s)
        print(any(truth))
    else: 
        print(False, False, sep = "\n")
