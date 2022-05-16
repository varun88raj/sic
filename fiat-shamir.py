import sympy
import random

MAX_VAL = 2**16
MIN_VAL = 2**8

p = sympy.randprime(MIN_VAL, MAX_VAL)
q = sympy.randprime(MIN_VAL, MAX_VAL)
n = p * q
print("P:" , p)
print("Q:" , q)
print("n:" , n)
s = random.randrange(2,n-2)
v = s**2 % n

print("s:" , s)
print("v:" , v)

r = random.randrange(1,n-1)
x = r**2 % n
c = random.randint(0,1)
y = r * (s**c) % n

print("x:" , x)
print("y:" , y)

check_1 = y**2 % n
check_2 = x*(v**c) % n

print("VALUES TO BE COMPARED:", check_1, ",", check_2)

if check_1 == check_2:
    print("Probable")
else:
    print("Improbable")