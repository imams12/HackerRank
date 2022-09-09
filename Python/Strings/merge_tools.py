## Solution 1
def merge_the_tools(string, k):
    n = len(string)
    awal = 0
    for i in range(0,n,k):
      t = string[i:i+k]
      u = ''
      for j in t:
        if j not in u:
          u += j
      print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

## Solution 2
import textwrap

def merge_the_tools(string, k):
    new = textwrap.wrap(string,k)
    final = ["".join([j[1] for j in enumerate(i) if j[1] not in i[:j[0]]]) for i in new] 
    print("\n".join(final))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
