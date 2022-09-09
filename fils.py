# with open ('/home/tajibay/dir.txt', 'r') as f:
#     print(f.read())

# with open ('text.txt', 'a') as f:
#     login = input('Введите логин: ')
#     f.write('Логин: \n')
#     f.write(login)
# print('OK')


# with open ('text.txt', 'r') as f_1:
#     f = f_1.read()


# with open ('users.txt', 'w') as f:
#     login = input('Введите логин: ')
#     parol = input('Введите пароль: ')
#     f.write('Логин: \n')
#     f.write(login)
#     f.write('\n') 
#     f.write('пароль: \n')
#     f.write(parol)
# print('OK')

# with open ('users.txt', 'r') as f:
#     for i in f:
#         if i == '123':
#             print('Да')
#         else:
#             print('Нет в тексте w')
# #    print(f.read())

# with open ('python.txt', 'w') as f:
#     f.write('Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.')
#     for i in f:
#         if i == 't':
#             t_words = ['i']
# print(t_words)

# with open ('file_1.txt', 'w') as f:
#     for i in range(5):
#         a = int(input('enter num: '))
#         f.write(f'{a} \n')
    
with open ('f_2.txt', 'w') as f:
    for i in range(10):
        a = input('введите текст:')
        if a == '':
            break
        else:
            f.write(f'{a}, ')
