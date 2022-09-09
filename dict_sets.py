# Словари

# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(6)
# print(dates_of_birth)

# set1 = {'bakai', 'nurdik', 'dair', 'mars', 'beka'}
# set2 = {'azat', 'bakai', 'alex', 'beka', 'mars'}
# set2.intersection_update(set1)
# print(set2)

# set2 = {'bakai', 'nurdik', 'dair', 'mars', 'beka'}
# set3 = {'azat', 'bakai', 'alex', 'beka', 'mars'}
# set2.difference_update(set3)
# print(set2)

# set_1 = {'bakai': 15, 'nurdik': 20, 'dair': 30, 'mars': 35, 'beka': 12}
# set_1['Tajibay'] = 46
# print(set_1)
# set_1.pop('bakai')
# print(set_1)

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_barmak'] = 130
# menu2 = {'lagman': 135}
# menu.update(menu2)

# print(menu)

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = 'Coca cola', 'Fanta', 'Sprite'
# print(menu)

# set1 = {'add', 'remove', 'update', 'clear', 'difference', 'discard', 'intersection', 'intersection_update', 'pop'}
# dict1 = {'clear', 'keys','items','get','values','update'}
# set1.intersection_update(dict1)
# print(set1)


# dict1 = {'stal':'politic','almaz':'president','aiba':'bankir','urmat':'itc','elmira':'rector'}
# for key, Value in dict1.items():
#    print(f'здравствуйте {key} у Вас прекрасная профессия {Value}')



# suitcase = []
# count = 0

# while True:
#     a = input('enter case: ')
#     count += 1
#     if count == 6:
#         break
#     else:
#         suitcase.append(a)
    
# print(suitcase)

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1.intersection_update(farm_2)
# print(farm_1)   


# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_2.difference_update(farm_1)
# print(farm_2)   

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia']
# south_american_countries2 = ['Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# a = set(south_american_countries)
# b = set(south_american_countries2)
# a.update(b)
# print(a)

#for i in range(1,11):
 #   print(f'цифра {i}')
  #  for j in range(1,11):
   #     print(f'{i} x {j} = {i * j}') 

# from multiprocessing.sharedctypes import Value


# dict1 = {
#     '12365545':{
#             'name': 'Alex',
#             'surname': 'Kavalsri',
#             'age': 30,
#             'gender':'M'
#         },
#     '65489777':{
#             'name': 'Aiba',
#             'surname': 'Kuvanch',
#             'age': 28,
#             'gender':'M'
#         },
#     '65498721':{
#             'name': 'Elmira',
#             'surname': 'Ismailvna',
#             'age': 48,
#             'gender':'F'
#         }
#    }

# for key in dict1:
#     print(key)
#     for value in dict1.values():
#         print(f'pasport: {key}  =  {value}')
