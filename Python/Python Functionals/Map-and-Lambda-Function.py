cube = lambda x: x**3

def fibonacci(n):
  # return a list of fibonacci numbers
  fib = []
  for i in range(n):
    if i == 0:
      fib.append(0) 
    elif i == 1 or i == 2:
      fib.append(1)
    elif i > 1:
      hasil = fib[i-1] + fib[i-2]
      fib.append(hasil)
  return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
