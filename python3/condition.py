import random

#if True: 
 #   print("ce message sera toujours affiché")

#if False:
# print("Ce message ne sera jamais affiché")



# if True: 
#     print("ce message sera toujours affiché")
# else:
#     print("Ce message ne sera jamais affiché")
# if False:
#     print("Ce message ne sera jamais affiché")
# else:
#     print("ce message sera toujours affiché")


# fruits = ['pomme', 'banane' , 'cerises']

# if 'pomme' in fruits:
#     print("Il y a des pommes")

# else:
#     print("il n'y a pas de pomme cassos")

# if 'orange' in fruits:
#     print("il y a des oranges")
# else:
#     print("qui a volé l'orange du marchant")


# is_authenticated = True

# if is_authenticated:
#     print("l'utilisateur peut accéser aux backoffice")

# user_password = "123"
# user_password_in_db = "abc"

# if user_password == user_password_in_db:
#     print("l'utilisateur peut accéder aux backoffice")
# else:
#     print("votre identifiant ou mot de passe ne correspond pas")

# user_in_db = [ 'toto', 'titi', 'tata', 'tutu']
# tutu_password_in_db = "adc"

# user_name_in_form = 'tutu'
# user_password_in_form = "123"

# if user_name_in_form in user_in_db and user_password_in_form == tutu_password_in_db:
#     print("l'utilisateur peut acceder aux backoffice")
# else:
#     print("identifiant ou mdp incorrect")

# electricity_is_off = bool(random.randint(0,1))
# water_is_off = bool(random.randint(0,1))
# gas_is_off = bool(random.randint(0,1))

# print('electricity_is_off:', electricity_is_off)
# print('water_is_off:', water_is_off)
# print('gas_is_off:', gas_is_off)

# if not electricity_is_off and not water_is_off and not gas_is_off: 
#     print("vous pouvez partir en weekend")
# else:
#     print("il reste des sources à couper")

#     if not electricity_is_off:
#             print("coupez l'éléctricité")

#     if not water_is_off:
#             print("coupez l'eau")

#     if not gas_is_off:
#             print("coupez le gaz")

# has_cash = bool(random.randint(0,1))
# has_card = bool(random.randint(0,1))
# has_check = bool(random.randint(0,1))

# if has_card or has_cash or has_check:
#     print("vous pouvez aller faire les courses")

#     if has_cash:
#         print("tu as du cash")
#     if has_card:
#         print("tu as ta carte")
#     if has_check:
#         print("tu as ton chequier")
# else:
#     print("rentre prendre ta carte tocard")

age = random.randint(0,100)

#0-5 bébé 
#6-11 enfant
#12-25 jeune
#26-59 adulte
#60+ senior 

if age <= 5:
    print("bébé")
elif 6 <= age <= 11:
    print("enfant")
elif 12 <= age <=25:
    print("jeune")
elif 26 <= age <=59: 
    print("adulte")
elif age >=60:
    print("senior")
