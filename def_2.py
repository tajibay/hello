# def kvadrat(x, n=2):
#     return x ** 2
# print(kvadrat(12,3))

# def login(name, age=20):
#     return f'ваше имя {name}, возраст {age}'
# print(login('Alex', 30))

# def add_1(x, y=2):
#     return x + y
# print(add_1(4, 6))

# def sabstract(x, y=2):
#     return x - y
# print(sabstract(4, 6))

# def multiply(x, y=2):
#     return x * y
# print(multiply(4, 6))

# def divide(x, y=2):
#     return x / y
# print(divide(4, 6))


# def str1():
#     count = 0
#     a = input('введите текст: ')
#     for i in a:
#         count += 1
#     print(count)
# str1()

# def merth(D1,D2):
#     py = {**D1,**D2}
#     return py
# D1 = {'name':'alex'}
# D2  = {'age': 45}
# D3 = merth(D1,D2)
# print(D3)

#def menu_1():
   # menu1 = input('что вы хотите заказать покушать и выпить: ')
  #  with open ('menu.txt', 'w') as f:
 #        f.write(menu1)
#         print(f'файл с именем menu.txt создан')
#menu_1()



# def func1():

#     a = input('enter file name: ')
#     with open (a, 'w') as f:
#         f.write('Hello')
#         print(f'файл с именем {a} создан')
# func1()

# import os
# os.system('rm -rf ssd.txt')

# def func_1():
#     return 'я главная функция'
# print(func_1())

# def func_2():
#     func_1()
#     return 'я вложенная функция'
# print(func_2())

# def dic_tup():
#     dict1 = {
#         'stal':'politic',
#         'almaz':'president',
#         'aiba':'bankir',
#         'urmat':'itc',
#         'elmira':'rector'}
#     tuple_1 = tuple(dict1.keys())
#     tuple_2 = tuple(dict1.values())
#     print(tuple_1)
#     print(tuple_2)
# dic_tup()

def chet_nechet(x):
     if x % 2 == 0:
      return f'{x} - четное'
      return f'{x} - не четное'


   
