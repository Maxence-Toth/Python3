import random 

# les types de boucle :
# while 
# do while 
# for classique 
# for each 
##############################################################

## boucle infinie ("boucle while)""

# counter = 1 ##afin de savoir combien de tour de boucle 

# # while True:
# print("tour:", counter)
# counter += 1


#######################################################################


##boucle "for" classique avec une "boucle while"

# #condition d'initialisation
# counter = 0  
# # taille de la boucle 
# limit = 10

# while True:
#     # condition d'arret
#     if counter >= limit:
#         break

#     #action à répéter 
#     print("tour:", counter)

#     # incrément / décrément
#     counter += 1

########################################################################

# #boucle "for"
# #condition d'initialisation
# counter = 0  
# # taille de la boucle 
# limit = 10

# while counter < limit:
#     #action à répéter 
#     print("tour:", counter)

#     # incrément / décrément
#     counter += 1

########################################################################

#boucle do while avec une boucle while 

# #condition d'initialisation
# counter = 0 
# # taille de la boucle 
# limit = 10 

# while True: 
#     #action à répéter
#     print("do while:", counter)

#     #incrément / décrément 

#     counter += 1

#     #condition de continuation 
#     if not (counter < limit):
#         break 

####################################################################
#algo tirage de 2 nombres différents parmis 5 


# numbers = []

# #1er tirage

# n = random.randint(1, 5)
# numbers.append(n)

# #2eme tirage
# while True:
#     n = random.randint(1, 5)

# #condition d'arret 

#     if n not in numbers:
#         #le nombre n'a pas encore été tiré au hasard
#         #ôn peut sortir de la boucle 
#         break




# numbers.append(n)

# print(numbers)


###########################################################

#boucle for de python 

# for counter in range(0, 10):

#     #action à répéter 
#     print('for python:', counter)

#####################################

#boucle for de python

# mots = ['foo', 'bar', 'baz']

# for i in range (0, len(mots)):
#     print('mot:', mots[i])

# for mot in mots:
#     print('mot:', mot)

# affichez les nombres de 100 à 999 avec une boucle for 

# for numbers in range(100,1000):
#     print(numbers)

#  affichez les nombres de 10 à 1 à rebours 

# for numbers in range(10,0,-1):
#     print(numbers)


#info : la fonction range() prend un troisieme parametre qui insique le 'pas' (step)
#[10:0:-1]

#affichez les nombre de 0 à 20 qui sont multiples de 3 

for numbers in range(0, 21, 3):
    print(numbers)