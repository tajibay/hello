
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b= a.count(13)
# c = len(a)
# if (b*100/c) < 70:
#    print('НЕУЖЕЛИ')
# elif (b*100/c) > 70:
#    print('Я ТАК И ЗНАЛ')
# else:
#    print('СОВПАДЕНИЕ? ТАК НЕ ДУМАЮ') 

# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key, value in dict1.items():
#     if value % 3 == 0:
#         print(f'{key} = hi')
#     elif value % 5 == 0:
#         print(f'{key} = bye')
#     else:
#         print(f' {key} value cannot be divided by 3 and 5')

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     a = languages.index(i)
#     print(f'{a} {i}')
    
# a = {}
# year = input('введите год: ')
# month = input('введите мес: ')
# date = input('введите число: ')
# time = input('введите время 18:30: ')
# a['год'] = year
# a['мес'] = month
# a['день'] = date
# a['время'] = time

# print(a)

# word = input('Введите слово: ').lower()
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопк    у',]
# for i in words:
#     if word == word[::-1]:
#         print('Является палиндромом')
# else:
#      print('Не является палиндромом')

#city = ['Bishkek', 'Osh', 'Batken', 'NewYork']

#commands = input('''Выберите действие:
# 1. Добавить 
# 2. Отобразить
# 3. Заменить город 
# 4. Удалить город
# 5. Выход \n>>> ''').lower()
# if commands == 'добавить':
#     new_city = input('Введите название города: ')
#     if new_city in city:
#         print('Такой город уже есть')
#     else:
#         city.append(new_city)
#         print(city)
# elif commands == 'отобразить':
#     print(city)
# elif commands == 'заменить город':
#     new_city = input('Введите название города на замену: ')
#     if new_city in city:
#         city.remove(new_city)
#         new_city = input('Введите новый город: ')
#         if new_city in city:
#             print('такой шород уже есть')
#         else:
#             city.append(new_city)
#         print(city)
# elif commands == 'удалить':
#     new_city = input('Введите название города на удаление: ')
#     city.remove(new_city)
#     print(city)
# elif commands == 'выход':
#     exit()
     

str1 = ('4729461084')
a = ','.join(str1)
print(type(a))