"""
Homework, task 2 for lesson
"""

# 1) Создать список из трех любых элементов.
lst = [0, 1, 2]
print(lst)

# 2) Создать словарь из трех пар ключ-значение.
dictionary = {'first':1, 'second':2, 'third':3}
print(dictionary)

# 3) Создать множество из трех элементов.
mnoj = set('aabbcc')
print(mnoj)

# 4) Из списка получить элемент с индексом 1
print(lst[1])

# 5) Написать условие if с двумя блоками elif и блоком else.
a = 3
b = 7
if a == 1 or b == 2:
    print('case 1')
elif a == 3 or b == 4:
    print('case 2')
elif a == 5 or b == 6:
    print('case 3')
else:
    print('case 4')


# 6) Написать цикл while.
a = ''
while len(a) < 10:
    a += 'a_'
print(a)

# 7) Создать список из трех элементов и распечать его элементы с помощью цикла for
lst = ['qwerty', 'asdfgh', 'zxcvbn']
for i in lst:
    print(i)

# 8) распечатать числа от 0 до 5
for i in range(6):
    print(i)

# 9) создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
str = 'TEST'
for i in str:
    if i =='E': print('pass')

# 10) Запросить данные у пользователя и распечатать их используя  форматированную строку.
text = input('what is your name: ')
print('User name is {0}'.format(text))

# 11) Распечатать содержимое файла
a = open("FileForTask02.txt", encoding="utf8")
print(a.read())

# 12) Создать функцию,которая принимает два аргумента, вернуть сумму двух аргументов.
def sum(arg1: int, arg2: int):
    return arg1 + arg2
print(sum(1,3))

# 13) Создать функцию, которая принимает любое количество параметров, распечатать эти параметры.
def return_args(*args):
    return print("Arguments: ", args)
return_args(1,2,3,4,5,5,6,7,8,8,9,9,8,6,5,9)




