# Mesurer la complexité d'un algo :
# via son efficacité 
# 1) Temps d'exécution (plus c'est court, mieux c'est)
# 2) Espace mémoire (plus c'est léger, mieux c'est)

# notation de Landau : O() ##c'est un o pas un zéro
# pas une fonction mais un ensemble 
#

#O(c) = constante
#O(1)
result = 123 + 42
print(result)

#O(n) 
#n est la quantité de données à traiter
numbers = [123, 42, 3.14]

for number in numbers :
    result = number * 2
    print(result)

numbers = [123, 42, 3.14]
more_numbers = [2.71, 3.14, 0, 53]
commun  = []

for number in numbers:       # pas le plus opti juste pour la démo
    for more_number in more_numbers:
        if number == more_number:
            commun.append(number)
print(commun)