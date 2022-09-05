def print_formatted(number):
    # your code goes here
    for i in range(1,n+1):
      lens = len(str(bin(n))) - 2
      pad = ' ' 
      a = str(i).rjust(lens,pad)
      b = str(oct(i)[2:]).rjust(lens,pad)
      c = str(hex(i)[2:]).upper().rjust(lens,pad)
      d = str(bin(i)[2:]).rjust(lens,pad)
      print(f'{a} {b} {c} {d}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
