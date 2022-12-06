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
# foo++ equivalant a foo += 1 mais cette operateur est utiliser en js en ph ou c++


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
# foo-- equivalant a foo -= 1 mais cette operateur est utiliser en js en ph ou c++

# * multiplication

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

# les operateur de comperaison
# ne pas confondre avec l'operateur d'afection et ne pas confondre === aevc l'identite' qui n'existe pas en python 

# l'egalité ==
foo =1 ==1
print (foo) 

# les grandeur 
foo = 123 < 42
print (foo)

# plus garnd  ou égale a 
foo =123 >= 42
print (foo)

# l'inegalité (ou différence)
foo = 123 != 42 
print(foo)

# les encadrement 
# < > <= >=
my_number = random.randint (0, 100)
foo = 4 <= my_number < 50
print(foo)
foo = 50 < my_number <= 100
print (foo)

# utilisation un peu "speciale" des comparaisons de grandeur 
foo = "abc" > "bcd"
print(foo)

# operateur and (et)
foo = True and False # false 
print (foo)
foo = False and True # false 
print(foo)
foo = True and True # true
print (foo)
foo = False and False # false 
print (foo)

a = random.randint (0, 1)
b = random.randint (0, 1)
foo = a and b 
print (a, b)
print (foo)

# operateur or (ou)
foo = True or False # true
print (foo)
foo = False or True # true 
print(foo)
foo = True or True # true
print (foo)
foo = False or False # false 
print (foo)

# operateur not (negation)
foo = not True
print (foo)
foo = not False
print (foo)
