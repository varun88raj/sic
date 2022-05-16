import random
import sympy

MAX_VAL = 2**16
MIN_VAL = 2**8

def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

def round(n,e):        
    r = random.randrange(2,n-2) 
    x = r**e % n
    print("x", x)
    c = random.randrange(1,e)
    y = (r*(s**c)) % n
    print("y", y)

    check = (y**e) * (v**c) % n

    print("Check value:", check)
    if check == x:
        print("Probable")
    else:
        print("Improbable")


p = sympy.randprime(MIN_VAL, MAX_VAL)
q = sympy.randprime(MIN_VAL, MAX_VAL)
n = p * q
phi = (p-1) * (q-1)

print("P", p)
print("Q", q)
print("n", n)
print("phi", phi)

e = 2
while(GCD(e,phi)!=1):
    e = e+1
s = 2
while(s<n-2):
    try:
        t = s**e
        v = pow(t, -1, n)
    except ValueError:
        v = None
    if(not v==None):
        break
    s=s+1

print("V", v)
for i in range(0,14):
    print("Round",i+1)
    round(n,e)

