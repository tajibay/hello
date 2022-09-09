# names = ['azat','bob','john','alex', 4,8,10]
# for i in names:
#     if i == 'bob':
#         names[names.index(i)] = 'arsen'
#     elif i == 8:
#         names[names.index(i)] = i + 8
# print(names)

a = []

while True:
    b = input('enter namber: ')
    if b == 'end':
        break
    else:
        a.append(b)

total = 0
for i in a:
    try:
        total += int(i)
    except ValueError:
        pass

print(f' Total: {total}')
print(f' Avergage: {total/len(a)}')
for i in a:
    print(i, end= ',')





