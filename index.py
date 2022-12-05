#!/bin/python
# int nombre entier 
my_number1 = 123
my_number2 = 42
my_number6 = 0 

print (my_number1)
print (my_number2)
print (my_number6)
print (type(my_number1))

# float nombre a virgule flottante 
my_number3 = 3.14
my_number4 = 2.71
# 0.0 ou 0. ou .0 
my_number5 = 0.0

print (my_number3)
print (my_number4)
print ( my_number5)
print (type(my_number3))

# bool , booléen 
my_boolean1 = True 
my_boolean2 = False
print (my_boolean1)
print (my_boolean2)
print (type(my_boolean1))

# None valeur nulle 
# null , nil
my_none = None 
print (my_none)
print (type(my_none))

# sting , chaine de caractéres
# double quote ou simple quote c'est pareill
my_texte1 = "ceci est une chaine de caractére"
my_texte2 = "ceci est une chaine de caractére"

print  (my_texte1)
print  (my_texte2)

# \ caratére d'echapement 
# \ n saut a la ligne 
my_texte3 = "abc\def\ghi"
my_texte4 = "John \"Foo\"  Doe"
print (my_texte3)
print (my_texte4)
print (type(my_texte1))

my_texte5 = """abc
def 
ghi 
"""
print (my_texte5)

my_texte6 = '''abc
def 
ghi 
'''
print (my_texte6)
print (type(my_texte5))

a = 123 
b = 42 
# permutation des variable 
a,b = b,a
print (a,b)

# transtypage 
# str vers int 
foo = "123"
foo = int(foo)
print (type(foo))

# str vers float 
foo = "123"
foo = float(foo)
print (type(foo))

# float vers int ,permet de suprimer tout ce qui ce trouve derriere la virgule 
foo = 3.14
foo = int(foo)
print (foo)

foo = 3.14 
# float vers str    
foo = str(foo)
print (foo)

#
foo = 2.71
# recuper la parti entiere 
a = ...
# recuprer la parti apres avec la vergile 
b = ...
print (a)
print (b)