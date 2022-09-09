# циклы - for, while
# names_num = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 124, 25, 600]
# for i in names_num :
#     print(i)

# name = ['Jack','Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 124, 25, 600]
# num = []
# leters = []
# for i in name:
#     if type(i) == str:
#         leters.append(i)
#     else:
#         num.append(i)
# print(leters)
# print(num)

# lang1 = 'go'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# #  Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
# for i in languages:
#     if i == lang1:
#         print('this languages is in list')
#     else:
#         break

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     else:
#         print(i)


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#     print(i)

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(len(languages)):
#     print(i, languages[i])

# a = [1,2,3,4,5]
# b = 7

# for i in a:
#     if i < 6:
#         print(b * b)    
#     else:
#         exit()


# a = list(range(1,20))
# for i in a:
#     if i > 9:
#         a.reverse()
#     print(i, end= ',')

# names = ('Максат', 'Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
# a = list(names)
# print(a[2::2])
# print(a[1::2])


# num = int(input('enter number: '))
# if num // 100 > 0:
#     print('трехзначное число ')
# else:
#     print('не трезначное ')
# if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Не четное число')
# if num % 31 == 0:
#     print('Делится на 31 ')
# else:
#     print('Не делится на 31')
# if num > 100 and num % 17 == 0 or num > 150 and num == 13002:
#     print(num) 


'''
numb = list(range(-100,100+1))
count = 0
# for i in numb:
#     if i % 13 == 0 and i % 2 == 0:
#         print(i, end= ',')
#         count += 1
# print(f' всего кол-во {count} цифр')

a  = numb[::7]
for i in a:
    if i % 2 == 0:
        print(i, end= ',')
        count += 1
print(f' всего кол-во {count} цифр')
'''

