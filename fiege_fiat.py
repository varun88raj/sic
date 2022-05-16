import sympy
import random
import math

MAX_VAL = 2**16
MIN_VAL = 2**8

def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

k=3

p = sympy.randprime(MIN_VAL, MAX_VAL)
q = sympy.randprime(MIN_VAL, MAX_VAL)
n = p * q
print("P:" , p)
print("Q:" , q)
print("n:" , n)
s=[]
v=[]


for i in range(k):
    temp=2
    while not(GCD(temp,n)==1) or temp in s:
        temp=temp+1
    temp1=pow(pow(temp, 2, n), -1, n)
    s.append(temp)
    v.append(temp1)
    

print("S:", s)
print("V:", v)

r = random.randrange(1,n-1)
x = r**2 % n
c=[]
for i in range(k):
    c.append(random.randrange(0,50))

print("C:", c)
y = r
for i in range(k):
    y*=(s[i]**c[i])

y = y % n

print("x:", x)
print("y:", y)

check = y**2
for i in range(k):
    check *= (v[i]**c[i])
check = check % n
    
print("Check Value:", check)

if check == x:
    print("Probable")
else:
    print("Improbable")