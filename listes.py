# text = "foo bar baz" 
# splitted_text = text.split(' ')

# print(splitted_text)
# print(len(splitted_text))
# result = splitted_text[0]
# splitted_text[0] = 'toto'
# #print(result)
# print(splitted_text)
# print(splitted_text[1])
# print(splitted_text[2])
# print(splitted_text[3]) # erreur 
# # splitted_text[3] = 123 # erreur

# splitted_text.append(123)
# print(splitted_text)

# # help(splitted_text.append)

# # [start:end:step]
# result = splitted_text[0:2]
# # start inclus
# # end exclus
# result = splitted_text[0:2]
# print(result)




text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

text = text.replace('.', '')
splitted_text = text.split(',')
my_text = ''.join(splitted_text)
splitted_my_text = text.split('.')
my_text = ''.join(splitted_text)



splitted_text = my_text.split(' ')
# print(len(splitted_text))


# #tous les mots de l'index 3 inclus à l'index 7 exclus
# partial_list = splitted_text[3:7]
# print(partial_list)
# print(splitted_text)

# #tous les mots de l'index 3 inclus à l'index 7 exclus avec un pas de 2
# partial_list = splitted_text[3:7:2]
# print(partial_list)
# print(splitted_text)


# # ATTENTION ne fonctionne pas dans l'autre sens 
# #tous les mots de l'index 7 inclus à l'index 3 exclus
# # l'index start doit être strictement inférieur à l'index end  
# partial_list = splitted_text[7:3]
# print(partial_list)
# print(splitted_text)

# start = 7
# end = 3 

# if start >= end:
#     start, end = end, start 

# print(start, end)
# partial_list = splitted_text[start:end]

# partial_liste = splitted_text[-7:-3]
# print(splitted_text)
# print(partial_list)



# partial_liste = splitted_text[-7:-3:2]

# print(splitted_text)
# print(partial_list)




# exo 
# 1. récupérez dans splitted_text les mots de l'index 35 à 49 inclus


short_text = splitted_text[35:50]
print(short_text)


# 2. affichez le numéro du dernier index 

print(len(splitted_text)+1)


# 3. récupérez 1 mot sur 2 de l'index 0 au dernier index 