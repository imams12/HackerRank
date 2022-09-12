# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())
x = z.real
y = z.imag

print(abs(complex(x, y)))
print(cmath.phase(complex(x, y)))
