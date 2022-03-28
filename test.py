import numbers
import math


# 1. Trois carrés pour le prix d'un

# 49 est un carré à deux chiffres. Si on le découpe en deux nombres
# 4 et 9, on obtient deux carrés à un chiffre. 49 est le seul carré a deux
# chiffres possédant cette particularité.
# Trouver 1'unique carré à quatre chiffres tel que ses deux premiers
# chiffres et ses deux derniers représentent deux carrés à deux chiffres.



L1 = [ n**2 for n in range (4,9+1)] #liste des carrés à 2 chiffres
L2 = [ n**2 for n in range (32,99+1)] #liste des carrés à 4 chiffres

reponse = []

for i in L2:
    if L2[:2] and L2[-2] in L1:
            reponse.append
print(reponse)




# du coup l2 = 'ABCD'
# checker que "AB" et "CD" se trouve dans L1 
# if true :
# stocker le résultat dans une variable "reponse"
# print reponse