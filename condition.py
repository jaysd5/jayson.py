import random

# if True :
    # print ("la condition est vraie")
    # print ("ce code est executer")

# if False :
    # print ("la condition est faux")
    # print ("ce code n'est pas executer")

# condition_vente = True

# if condition_vente == True :
   # print ("l'utilisateur a accepté les conditon de vente")
# else :
    # print ("l'utilasateur na pas accepter les conditiont de vente") 

# if condition_vente != True :
   # print ("l'utilisateur n'a pas accepté les condition de vente")

# if not condition_vente :
    # print ("l'utilisateur n'a pas accepté les condition de vente")
# else :
   # print ("l'utilisateur a accepté les conditon de vente")

emails = random.randint (0, 100)

# elif c'est la même chose que else if 
   
if emails == 1 : 
    print ("vous avez un nouveau mail")
elif emails > 1 :
    print (f"vous avez {emails} nouveau mail ")
else :
    print ("vous n'avez pas de nouveaux mail")
    

windows_closed = bool ( random.randint(0, 1))
electicity_off = bool ( random.randint(0, 1))

print (f'{windows_closed=}')
print (f'{electicity_off=}')


if windows_closed and electicity_off :
    print ("les fenetre sont fermées")
    print ("l'electriciter est fermées")
elif not windows_closed and electicity_off : 
    print ("les fenetre sont pas fermées")
    print ("l'electriciter est fermées")
elif windows_closed and not electicity_off : 
    print ("les fenetre sont fermées")
    print ("l'electriciter n'ait pas  fermées")
else :
    print ("les fenetre sont pas fermées")
    print ("l'electriciter n'ait pas fremées")