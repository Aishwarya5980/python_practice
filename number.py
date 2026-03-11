a=5
b=56.56
c=85+5j
print(type(a))
print(type(b))
print(type(c))
print(int(b))
print(int(c.real))
print(int(c.imag))
price=532145.8542
print(abs(price))
print(round(price))

import math
print(math.ceil(price))
print(math.floor(price))
print(math.trunc(price))

import random
print(random.random())
print(random.randint(1,6))

print((5).is_integer())
print(isinstance(5, str))

a=5
b=5
print(a is b)

a=[1,2,3]
b=[1,2,3]
print(a is b)
