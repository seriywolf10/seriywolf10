# Taylor series again :)
# now we find cos(x)
# the bigger n , the better accuracy
# although we could take my previous programm on taylor series 
# and just do sqrt(1 - sin**2)

from math import factorial

x = float(input('enter degrees '))
x = x * 3.1415926535 / 180 # Convert degrees to radians 

n = 20 # the max number of iterations to prevent overflow
cos = 0

for i in range(0, n + 1):
    cos += (((-1)**i) * (x**(2*i))) / (factorial(2*i))
    
print(cos)
