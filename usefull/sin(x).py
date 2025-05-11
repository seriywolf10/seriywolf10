# the taylor series code
# it approximates the value of sin(x) 
# the bigger value of n, the better
from math import factorial
x = float(input())
n = int(input())
sin = 0

for i in range(0, n+1):
    sin += (-1)**i *x ** (2*i +1)/factorial(2*i+1)

print(s)
        
