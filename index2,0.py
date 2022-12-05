import random
import math

# = affectation
foo = 123

# + addition
foo = 123 + 42 
foo = foo + 42
# += operateur d'incrémentation 
foo += 42
print (foo)

# / division 
foo = 123 / 42
foo /= 42
print (foo)

# // division entière
foo = 142 // 42
foo //= 42
print (type(foo))

# - soutraction 
foo = 123 - 42
foo = foo - 42
print (foo)
# -= operateur de décrémentation 
foo -= 42
print (foo)

# * multiplication
#  
# ** puissance 
foo = 2 ** 2
foo = 2 ** 3  
foo **= 6
print  (foo)


# % modulo 
foo = 123 % 23
foo = foo % 23
foo %= 23
foo = random.randint(1,100)
print (foo % 2)
print (foo)

# sqrt () racine carré 
foo = math.sqrt (4) 
# 0.5 / 1/2 / 1.3 = rascine cubique 
foo = 4 ** 0.5
foo = 4 ** (1/2)
foo = 8 ** (1/3)
print (foo)


# ^ puissance mais pas en python 